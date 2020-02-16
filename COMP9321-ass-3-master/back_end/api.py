"""
    REST API for the population prediction system.
"""

from flask import Flask, request
from flask_restplus import Resource, Api
import os
from pymongo import MongoClient
import secrets
from datetime import datetime
from flask_cors import CORS

from static import *
import machine

"""
    Initial Setup
"""


app = Flask(__name__)
CORS(app)
api = Api(app)
ml_client = MongoClient(host=MDB_HOST)
ml_db = ml_client.get_database()


"""
    Validity Checks
"""
def isValidState(state):
    return state in STATE_NAMES

def isValidRegion(region):
    return region in REGION_NAMES

def isValidPredictYear(year):
    return year in range(*PREDICTION_RANGE)



"""
    Decorators for validating endpoint variables and checking token
      logins.
"""

def requiresValidRegion(f):
    def funcWrapper(*args, **kws):
        region = kws['region']
        if not isValidRegion(region):
            return api.abort(400,
                "The region passed is invalid. See %s for a list of valid regions" % (
                    os.path.join(api.base_url,'regions')))
        return f(*args, **kws)
    return funcWrapper


def requiresValidYear(f):
    def funcWrapper(*args, **kws):
        year = kws['year']
        if not isValidPredictYear(year):
            return api.abort(400, "The year passed must be in the range %s" % (repr(PREDICTION_RANGE)))
        return f(*args,**kws)
    return funcWrapper


def requiresValidToken(f):
    def funcWrapper(*args, **kws):
        # checks MongoDB database for a valid token
        token = request.args.get("token")
        if token != None:
            returned = ml_db[MDB_COL_TOKENS].find_one({'token' : token})
            if returned != None: 
                return f(*args, **kws)
        return api.abort(401, 'A valid authentication token has not been provided')
    return funcWrapper

@api.route('/prediction/<int:year>')
class predictAustralia(Resource):
    """
        Returns a prediction for Australia.
    """
    @requiresValidToken
    @requiresValidYear
    def get(self, year):

        results = list(machine.prediction_region(year))
        au_res = results[list(REGION_NAMES).index('AUS')]
        return {'region' : 'AUS', 'num_results' : 1,
                'results' : {
                    'AUS' : {'value' : au_res, 'proportion' : 1.0},
                }
            }



@api.route('/prediction/<int:year>/states')
class predictStates(Resource):
    """
        Returns a prediction for each state/territory.
    """
    @requiresValidToken
    @requiresValidYear
    def get(self, year):

        vals = list(machine.prediction_region(year))[1:] # ignore AUS (first) result
        keys = REGION_NAMES[1:]

        results = dict(zip(keys,vals))
        total = sum(vals)
        results = {k : {'value':v, 'proportion' : round(v/total, 4)} for k,v in results.items()}

        return {'num_results' : len(results),
                'results' : results
            }



@api.route('/prediction/<int:year>/genders/<string:region>')
class predictGenders(Resource):
    """
        Returns a prediction for each gender, for a particular state.
    """
    @requiresValidToken
    @requiresValidYear
    @requiresValidRegion
    def get(self, year, region):

        males, females = list(machine.prediction_gender(region, year))
        total = males + females

        return {'region' : region, 'num_results' : 2,
                'results' : {
                    'MALES' : {'value' : males, 'proportion' : round(males/total,4)},
                    'FEMALES' : {'value' : females, 'proportion' : round(females/total,4)},
                }
            }


@api.route('/prediction/<int:year>/ages/<string:region>')
class predictAges(Resource):
    """
        Returns a prediction for each age_band, for a particular state.
    """
    @requiresValidToken
    @requiresValidYear
    @requiresValidRegion
    def get(self, year, region):

        vals = list(machine.prediction_age(region,year))
        keys = AGE_BANDS

        results = dict(zip(keys,vals))
        total = sum(vals)
        results = [{'title':k, 'value':v, 'proportion' : round(v/total, 4)} for k,v in results.items()]


        return {'region' : region, 'num_results' : len(results),
                'results' : results
            }

@api.route('/regions')
class listRegions(Resource):
    """
        Lists each region with some metadata.
    """
    @requiresValidToken
    def get(self):
        return REGIONS_INFO


@api.route('/tokens/new')
class autheticationToken(Resource):
    """
        Creates an authetication token (requires user/pass verification)
    """
    def get(self):
        user = request.args.get('username')
        passw = request.args.get('password')

        if user == ADMIN_USER and passw == ADMIN_PASS:
            # keep generating random tokens until we don't have a duplicate
            temp_token = secrets.token_urlsafe(16)
            while ml_db[MDB_COL_TOKENS].find_one({'token' : temp_token}) != None:
                temp_token = secrets.token_urlsafe(16)

            token_out = {'token' : temp_token,
                         'time_created' : datetime.now().isoformat(),
                         'created_by' : user}
            ml_db[MDB_COL_TOKENS].insert_one(token_out)

            # return the token with meta data (without MongoDB "_id")
            return {x:y for x,y in token_out.items() if not x.startswith('_')}
        return api.abort(401, 'A valid username and password has not been provided')


if __name__ == '__main__':
    app.run(debug=False)

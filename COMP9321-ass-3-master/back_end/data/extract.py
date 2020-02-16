"""
    Retrieves data from MongoDB (data cleansed and generated in extract.py)
"""

from pymongo import MongoClient
import pandas

MDB_HOST = "mongodb://admin:9321admin@ds131763.mlab.com:31763/9321-ass-3"
MDB_COL_DATA = "raw_data"
MDB_DOC_REGIONS = "regions"
MDB_DOC_AGES = "age_%s"
MDB_DOC_GENDERS = "gender_%s"

ml_client = MongoClient(host=MDB_HOST)
ml_db = ml_client.get_database()
ml_col = ml_db[MDB_COL_DATA]

def get_region_data():
    return _generate_df(ml_col.find_one({'id' : MDB_DOC_REGIONS}))


def get_age_data(region):
    return _generate_df(ml_col.find_one({'id' : MDB_DOC_AGES % (region)}))

def get_gender_data(region):
    return _generate_df(ml_col.find_one({'id' : MDB_DOC_GENDERS % (region)}))

"""
    Extracts dataframe from Mongo-returned JSON
"""
def _generate_df(di):
    if di == None:
        raise ValueError('The document could not be found (most likely due to an invalid region being provided)')

    return pandas.DataFrame.from_dict(di['data']).rename(index=int)

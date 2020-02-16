
from pymongo import MongoClient
import pandas 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd   
import numpy as np  
import matplotlib.pyplot as plt
import math
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
def get_gender_data(region):
    return _generate_df(ml_col.find_one({'id' : MDB_DOC_GENDERS % (region)}))
def get_age_data(region):
    return _generate_df(ml_col.find_one({'id' : MDB_DOC_AGES % (region)}))
def _generate_df(di):
    if di == None:
        raise ValueError('The document could not be found (most likely due to an invalid region being provided)')
    return pandas.DataFrame.from_dict(di['data']).rename(index=int)
## An explanatory variable is a variable that have impact to determine the value of the population

def model(state):
    data = get_region_data()
    df = pd.DataFrame(data)
    df['S_2'] = df[state].shift(1).rolling(window = 2).mean()   
    df['S_3'] = df[state].shift(1).rolling(window = 3).mean()
    df['S_4'] = df[state].shift(1).rolling(window = 4).mean()
    df['S_5'] = df[state].shift(1).rolling(window = 5).mean()
    df['S_6'] = df[state].shift(1).rolling(window = 6).mean()
    df= df.dropna()
    X = df[['S_2','S_3','S_4','S_5','S_6']]   
    y = df[state] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0) 
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    return model

def model_gender(state, gender):
    data = get_gender_data(state)
    df = pd.DataFrame(data)
    if gender == 'MALES':
        df['S_2'] = df[gender].shift(1).rolling(window = 2).mean()   
        df['S_3'] = df[gender].shift(1).rolling(window = 3).mean()
        df['S_4'] = df[gender].shift(1).rolling(window = 4).mean()
        df['S_5'] = df[gender].shift(1).rolling(window = 5).mean()
        df['S_6'] = df[gender].shift(1).rolling(window = 6).mean()
    if gender == 'FEMALES':
        df['S_2'] = df[gender].shift(1).rolling(window = 2).mean()   
        df['S_3'] = df[gender].shift(1).rolling(window = 3).mean()
        df['S_4'] = df[gender].shift(1).rolling(window = 4).mean()
        df['S_5'] = df[gender].shift(1).rolling(window = 5).mean()
        df['S_6'] = df[gender].shift(1).rolling(window = 6).mean()

    df= df.dropna()
    X = df[['S_2','S_3','S_4','S_5','S_6']]   
    y = df[gender] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0) 
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    return model


def model_age(region, age):
    data = get_age_data(region)
    df = pd.DataFrame(data)
    df['S_2'] = df[age].shift(1).rolling(window = 2).mean()   
    df['S_3'] = df[age].shift(1).rolling(window = 3).mean()
    df['S_4'] = df[age].shift(1).rolling(window = 4).mean()
    df['S_5'] = df[age].shift(1).rolling(window = 5).mean()
    df['S_6'] = df[age].shift(1).rolling(window = 6).mean()
    df= df.dropna()
    X = df[['S_2','S_3','S_4','S_5','S_6']]   
    y = df[age] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0) 
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    return model


def prediction_region(state, year):
    return int(model(state).predict([[year]]))

def prediction_gender(state, gender, year):
    return int(model_gender(state, gender).predict([[year]]))

def prediction_age(region, age, year):
        return int(model_age(region, age).predict([[year]]))










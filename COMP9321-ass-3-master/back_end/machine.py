
from pymongo import MongoClient
import pandas 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd   
import numpy as np  

from data.extract import *

def model(year):
    data = get_region_data()
    df = pd.DataFrame(data)
##AUS
    df['S_2'] = df['AUS'].shift(1).rolling(window = 3).mean()
    df['S_3'] = df['AUS'].shift(1).rolling(window = 3).mean()
    df['S_4'] = df['AUS'].shift(1).rolling(window = 4).mean()
    df['S_5'] = df['AUS'].shift(1).rolling(window = 5).mean()
    df['S_6'] = df['AUS'].shift(1).rolling(window = 6).mean()
##NSW
    df['S_7'] = df['NSW'].shift(1).rolling(window = 3).mean()
    df['S_8'] = df['NSW'].shift(1).rolling(window = 3).mean()
    df['S_9'] = df['NSW'].shift(1).rolling(window = 4).mean()
    df['S_10'] = df['NSW'].shift(1).rolling(window = 5).mean()
    df['S_11'] = df['NSW'].shift(1).rolling(window = 6).mean()
##VIC
    df['S_12'] = df['VIC'].shift(1).rolling(window = 3).mean()
    df['S_13'] = df['VIC'].shift(1).rolling(window = 3).mean()
    df['S_14'] = df['VIC'].shift(1).rolling(window = 4).mean()
    df['S_15'] = df['VIC'].shift(1).rolling(window = 5).mean()
    df['S_16'] = df['VIC'].shift(1).rolling(window = 6).mean()
##QLD
    df['S_17'] = df['QLD'].shift(1).rolling(window = 3).mean()
    df['S_18'] = df['QLD'].shift(1).rolling(window = 3).mean()
    df['S_19'] = df['QLD'].shift(1).rolling(window = 4).mean()
    df['S_20'] = df['QLD'].shift(1).rolling(window = 5).mean()
    df['S_21'] = df['QLD'].shift(1).rolling(window = 6).mean()
##SA
    df['S_22'] = df['SA'].shift(1).rolling(window = 3).mean()
    df['S_23'] = df['SA'].shift(1).rolling(window = 3).mean()
    df['S_24'] = df['SA'].shift(1).rolling(window = 4).mean()
    df['S_25'] = df['SA'].shift(1).rolling(window = 5).mean()
    df['S_26'] = df['SA'].shift(1).rolling(window = 6).mean()
##WA
    df['S_27'] = df['WA'].shift(1).rolling(window = 3).mean()
    df['S_28'] = df['WA'].shift(1).rolling(window = 3).mean()
    df['S_29'] = df['WA'].shift(1).rolling(window = 4).mean()
    df['S_30'] = df['WA'].shift(1).rolling(window = 5).mean()
    df['S_31'] = df['WA'].shift(1).rolling(window = 6).mean()
##TAS
    df['S_32'] = df['TAS'].shift(1).rolling(window = 3).mean()
    df['S_33'] = df['TAS'].shift(1).rolling(window = 3).mean()
    df['S_34'] = df['TAS'].shift(1).rolling(window = 4).mean()
    df['S_35'] = df['TAS'].shift(1).rolling(window = 5).mean()
    df['S_36'] = df['TAS'].shift(1).rolling(window = 6).mean()
##NT
    df['S_37'] = df['NT'].shift(1).rolling(window = 3).mean()
    df['S_38'] = df['NT'].shift(1).rolling(window = 3).mean()
    df['S_39'] = df['NT'].shift(1).rolling(window = 4).mean()
    df['S_40'] = df['NT'].shift(1).rolling(window = 5).mean()
    df['S_41'] = df['NT'].shift(1).rolling(window = 6).mean()
##ACT
    df['S_42'] = df['ACT'].shift(1).rolling(window = 3).mean()
    df['S_43'] = df['ACT'].shift(1).rolling(window = 3).mean()
    df['S_44'] = df['ACT'].shift(1).rolling(window = 4).mean()
    df['S_45'] = df['ACT'].shift(1).rolling(window = 5).mean()
    df['S_46'] = df['ACT'].shift(1).rolling(window = 6).mean()
    df = df.dropna()
    X = df[['S_2','S_3','S_4','S_5','S_6']]
    X1 = df[['S_7','S_8','S_9','S_10','S_11']]
    X2 = df[['S_12','S_13','S_14','S_15','S_16']]
    X3 = df[['S_17','S_18','S_19','S_20','S_21']]
    X4 = df[['S_22','S_23','S_24','S_25','S_26']]
    X5 = df[['S_27','S_28','S_29','S_30','S_31']]
    X6 = df[['S_32','S_33','S_34','S_35','S_36']]
    X7 = df[['S_37','S_38','S_39','S_40','S_41']]
    X8 = df[['S_42','S_43','S_44','S_45','S_46']]
    y = df['AUS']
    y1 = df['NSW']
    y2 = df['VIC']
    y3 = df['QLD']
    y4 = df['SA']
    y5 = df['WA']
    y6 = df['TAS']
    y7 = df['NT']
    y8 = df['ACT'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0)
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.72, random_state = 0)
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.72, random_state = 0)
    X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.72, random_state = 0)
    X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y4, test_size=0.72, random_state = 0)
    X5_train, X5_test, y5_train, y5_test = train_test_split(X5, y5, test_size=0.72, random_state = 0)
    X6_train, X6_test, y6_train, y6_test = train_test_split(X6, y6, test_size=0.72, random_state = 0)
    X7_train, X7_test, y7_train, y7_test = train_test_split(X7, y7, test_size=0.72, random_state = 0)
    X8_train, X8_test, y8_train, y8_test = train_test_split(X8, y8, test_size=0.72, random_state = 0) 
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    model1 = LinearRegression().fit(X1_train.index.values.reshape(-1, 1), y1_train)
    model2 = LinearRegression().fit(X2_train.index.values.reshape(-1, 1), y2_train)
    model3 = LinearRegression().fit(X3_train.index.values.reshape(-1, 1), y3_train)
    model4 = LinearRegression().fit(X4_train.index.values.reshape(-1, 1), y4_train)
    model5 = LinearRegression().fit(X5_train.index.values.reshape(-1, 1), y5_train)
    model6 = LinearRegression().fit(X6_train.index.values.reshape(-1, 1), y6_train)
    model7 = LinearRegression().fit(X7_train.index.values.reshape(-1, 1), y7_train)
    model8 = LinearRegression().fit(X8_train.index.values.reshape(-1, 1), y8_train)
    a = int(model.predict([[year]]))
    n = int(model1.predict([[year]]))
    v = int(model2.predict([[year]]))
    q = int(model3.predict([[year]]))
    s = int(model4.predict([[year]]))
    w = int(model5.predict([[year]]))
    t = int(model6.predict([[year]]))
    n = int(model7.predict([[year]]))
    act = int(model8.predict([[year]]))
    return a, n, v, q, s, w, t, n, act

def model_gender(state, year):
    data = get_gender_data(state)
    df = pd.DataFrame(data)
    df['S_2'] = df['MALES'].shift(1).rolling(window = 2).mean()   
    df['S_3'] = df['MALES'].shift(1).rolling(window = 3).mean()
    df['S_4'] = df['MALES'].shift(1).rolling(window = 4).mean()
    df['S_5'] = df['MALES'].shift(1).rolling(window = 5).mean()
    df['S_6'] = df['MALES'].shift(1).rolling(window = 6).mean()
    df['S_7'] = df['FEMALES'].shift(1).rolling(window = 2).mean()   
    df['S_8'] = df['FEMALES'].shift(1).rolling(window = 3).mean()
    df['S_9'] = df['FEMALES'].shift(1).rolling(window = 4).mean()
    df['S_10'] = df['FEMALES'].shift(1).rolling(window = 5).mean()
    df['S_11'] = df['FEMALES'].shift(1).rolling(window = 6).mean()
    df= df.dropna()
    X = df[['S_2','S_3','S_4','S_5','S_6']]
    X1 = df[['S_2','S_3','S_4','S_5','S_6']]   
    y = df['MALES']
    y1 = df['FEMALES']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0)
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.72, random_state = 0) 
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    model1 = LinearRegression().fit(X1_train.index.values.reshape(-1, 1), y1_train)
    m = int(model.predict([[year]]))
    f = int(model1.predict([[year]]))
    return m, f


def model_age(region, year):
    data = get_age_data(region)
    df = pd.DataFrame(data)

    df= df.dropna()
    X = df[['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85 and over']]   
    y = df['0-4']
    y1 = df['5-9']
    y2 = df['10-14']
    y3 = df['15-19']
    y4 = df['20-24']
    y5 = df['25-29']
    y6 = df['30-34']
    y7 = df['35-39']
    y8 = df['40-44']
    y9 = df['45-49']
    y10 = df['50-54']
    y11 = df['55-59']
    y12 = df['60-64']
    y13 = df['65-69']
    y14 = df['70-74']
    y15 = df['75-79']
    y16 = df['80-84']
    y17 = df['85 and over']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72, random_state = 0) 
    X_train, X_test, y1_train, y_test = train_test_split(X, y1, test_size=0.72, random_state = 0)
    X_train, X_test, y2_train, y_test = train_test_split(X, y2, test_size=0.72, random_state = 0)
    X_train, X_test, y3_train, y_test = train_test_split(X, y3, test_size=0.72, random_state = 0)
    X_train, X_test, y4_train, y_test = train_test_split(X, y4, test_size=0.72, random_state = 0)
    X_train, X_test, y5_train, y_test = train_test_split(X, y5, test_size=0.72, random_state = 0)
    X_train, X_test, y6_train, y_test = train_test_split(X, y6, test_size=0.72, random_state = 0)
    X_train, X_test, y7_train, y_test = train_test_split(X, y7, test_size=0.72, random_state = 0)
    X_train, X_test, y8_train, y_test = train_test_split(X, y8, test_size=0.72, random_state = 0)
    X_train, X_test, y9_train, y_test = train_test_split(X, y9, test_size=0.72, random_state = 0)
    X_train, X_test, y10_train, y_test = train_test_split(X, y10, test_size=0.72, random_state = 0)
    X_train, X_test, y11_train, y_test = train_test_split(X, y11, test_size=0.72, random_state = 0)
    X_train, X_test, y12_train, y_test = train_test_split(X, y12, test_size=0.72, random_state = 0)
    X_train, X_test, y13_train, y_test = train_test_split(X, y13, test_size=0.72, random_state = 0)
    X_train, X_test, y14_train, y_test = train_test_split(X, y14, test_size=0.72, random_state = 0)
    X_train, X_test, y15_train, y_test = train_test_split(X, y15, test_size=0.72, random_state = 0)
    X_train, X_test, y16_train, y_test = train_test_split(X, y16, test_size=0.72, random_state = 0)
    X_train, X_test, y17_train, y_test = train_test_split(X, y17, test_size=0.72, random_state = 0)
    
    model = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y_train)
    model1 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y1_train)
    model2 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y2_train)
    model3 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y3_train)
    model4 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y4_train)
    model5 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y5_train)
    model6 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y6_train)
    model7 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y7_train)
    model8 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y8_train)
    model9 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y9_train)
    model10 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y10_train)
    model11 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y11_train)
    model12 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y12_train)
    model13 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y13_train)
    model14 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y14_train)
    model15 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y15_train)
    model16 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y16_train)
    model17 = LinearRegression().fit(X_train.index.values.reshape(-1, 1), y17_train)

    a = int(model.predict([[year]]))
    a1= int(model1.predict([[year]]))
    a2 = int(model2.predict([[year]]))
    a3 = int(model3.predict([[year]]))
    a4 = int(model4.predict([[year]]))
    a5 = int(model5.predict([[year]]))
    a6 = int(model6.predict([[year]]))
    a7 = int(model7.predict([[year]]))
    a8 = int(model8.predict([[year]]))
    a9 = int(model9.predict([[year]]))
    a10 = int(model10.predict([[year]]))
    a11 = int(model11.predict([[year]]))
    a12 = int(model12.predict([[year]]))
    a13 = int(model13.predict([[year]]))
    a14 = int(model14.predict([[year]]))
    a15 = int(model15.predict([[year]]))
    a16 = int(model16.predict([[year]]))
    a17 = int(model17.predict([[year]]))
    return a, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17


def prediction_region(year):
    a, n, v, q, s, w, t, n, act = model(year)
    return a, n, v, q, s, w, t, n, act

def prediction_gender(state, year):
    m, f = model_gender(state, year)
    return m, f

def prediction_age(region, year):
    a, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17 = model_age(region, year)
    return a, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17




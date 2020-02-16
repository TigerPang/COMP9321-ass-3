from pymongo import MongoClient
from sklearn.model_selection import train_test_split
import pandas as pd
import pandas 
import numpy as np  
import matplotlib.pyplot as plt
from sklearn import model_selection

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
df = pd.DataFrame(get_region_data())
df['S_2'] = df['NSW'].shift(1).rolling(window = 2).mean()   
df['S_3'] = df['NSW'].shift(1).rolling(window = 3).mean()
df['S_4'] = df['NSW'].shift(1).rolling(window = 4).mean()
df['S_5'] = df['NSW'].shift(1).rolling(window = 5).mean()
df['S_6'] = df['NSW'].shift(1).rolling(window = 6).mean()
df= df.dropna()
X = df[['S_2','S_3','S_4','S_5','S_6']] 
y = df.index
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.72,random_state=0)

from sklearn.linear_model import LinearRegression
lin = LinearRegression().fit(X_train, y_train)
print('Accuracy of LinearRegression classifier on training set: {:.2f}'
     .format(lin.score(X_train, y_train)))

from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, y_train)
print('Accuracy of KNeighbors on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))

from sklearn.linear_model import LogisticRegression
log = LogisticRegression().fit(X_train, y_train)
print('Accuracy of LogisticRegression on training set: {:.2f}'
     .format(log.score(X_train, y_train)))

print(' ')
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
y_pred = lin.predict(X_test)
print('The mean absolute error for LinearRegression is: {:.2f}'
     .format(mean_absolute_error(y_test,y_pred)))
print('The explained variance score for LinearRegression is: {:.2f}'
     .format(explained_variance_score(y_test,y_pred)))
           
y_pred = knn.predict(X_test)
print('The mean absolute error for KNeighbors is: {:.2f}'
     .format(mean_absolute_error(y_test,y_pred)))
print('The explained variance score for KNeighbors is: {:.2f}'
     .format(explained_variance_score(y_test,y_pred)))

y_pred = log.predict(X_test)
print('The mean absolute error for LogisticRegression is: {:.2f}'
     .format(mean_absolute_error(y_test,y_pred)))
print('The explained variance score for LogisticRegression is: {:.2f}'
     .format(explained_variance_score(y_test,y_pred)))



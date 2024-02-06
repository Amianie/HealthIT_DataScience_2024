#!/usr/bin/env python3

# importing packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# importing data
data=pd.read_csv('Scikit_learn/AmesHousing.csv')
print(data.shape)

# dropping rows which have null values
data.dropna(inplace=True,axis=0)

X= data['PID']
y=data['Lot Area']

#y = df['Lot Area']
#X = df.drop('Lot Area',axis=1)

# splitting the dataframe into train and test sets
#X_train,X_test,y_train,y_test = train_test_split(
 # X,y,test_size=0.3,random_state=101)
#scaler = StandardScaler()
#scaler.fit(X_train)
#X_train = scaler.transform(X_train)
#X_test = scaler.transform(X_test)

#Simple linear regression model
#model = LinearRegression().fit(X_train,y_train)
#y_pred = model.predict(X_test)
#print(y_pred)
#print(mean_squared_error(y_test,y_pred))
 

# using the train test split function
X_train, X_test, y_train, y_test = train_test_split(
X,y , random_state=104,test_size=0.25, shuffle=True)

print('X_train : ')
print(X_train.head())
print(X_train.shape)

print('')
print('X_test : ')
print(X_test.head())
print(X_test.shape)

print('')
print('y_train : ')
print(y_train.head())
print(y_train.shape)

print('')
print('y_test : ')
print(y_test.head())
print(y_test.shape)

# head of the data
print('Head of the dataframe : ')
print(data.head())

print(data.columns)


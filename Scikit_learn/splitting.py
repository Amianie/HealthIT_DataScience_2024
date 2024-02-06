#!/usr/bin/env python3
from sklearn.datasets import fetch_california_housing

housing_data = fetch_california_housing()
X = housing_data.data # represent the feature matrix
y = housing_data.target # represent the response vector/target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)
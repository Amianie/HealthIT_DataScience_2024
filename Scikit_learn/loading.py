#!/usr/bin/env python3

import pandas as pd

# Load data from your local CSV file
csv_path = 'AmesHousing.csv'  # Replace with your file path
housing_data = pd.read_csv('AmesHousing.csv')

# Extract feature matrix and target vector
X = housing_data.drop('Overall Cond', axis=1)  # Replace 'target_column_name' with your actual target column name
y = housing_data['Overall Cond']

# Assuming feature_names are the column names of X
feature_names = X.columns.tolist()

print('Feature names: ', feature_names)
print('\nTarget name: ', 'Overall Cond', '(Overal Condition)')  # Replace with your actual target column name
print("\nFirst 5 rows of X:\n", X.head())
print('\nShape of dataset', X.shape)
print ('Hello World!')
prin
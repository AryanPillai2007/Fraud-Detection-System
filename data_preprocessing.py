#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:35:00 2023

@author: aryanpillai2701
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Step 1: Load the dataset and perform initial preprocessing
dataset = pd.read_csv('/Users/aryanpillai2701/Library/On Disk/Files/ISM/creditcard.csv')

# Step 2: Feature Scaling
scaler = StandardScaler()
dataset['Amount'] = scaler.fit_transform(dataset['Amount'].values.reshape(-1, 1))

# Step 3: Data Splitting
X = dataset.drop('Class', axis=1)
y = dataset['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed data and split datasets
X_train.to_csv('train_data.csv', index=False)
X_test.to_csv('test_data.csv', index=False)
y_train.to_csv('train_labels.csv', index=False)
y_test.to_csv('test_labels.csv', index=False)

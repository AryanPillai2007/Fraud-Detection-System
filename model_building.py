#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:33:46 2023

@author: aryanpillai2701
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the preprocessed training data and labels
X_train = pd.read_csv('train_data.csv')
y_train = pd.read_csv('train_labels.csv')

# Initialize and train a Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train.values.ravel())

# Save the trained model to a file
joblib.dump(classifier, 'fraud_detection_model.pkl')

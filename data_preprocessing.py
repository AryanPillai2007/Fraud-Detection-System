import pandas as pd
import numpy as np

# Load the dataset
dataset = pd.read_csv('financial_transactions.csv')

# Data cleaning: handle missing values, duplicates, and outliers
dataset.drop_duplicates(inplace=True)
dataset.dropna(inplace=True)

# Feature selection: choose relevant features
selected_features = ['transaction_amount', 'transaction_time', 'location', 'customer_behavior']
dataset = dataset[selected_features]

# Feature engineering: create additional features
# (You can add more feature engineering here)

# Data normalization/scaling if needed
# (You can add normalization/scaling here)

# Save the preprocessed dataset
dataset.to_csv('preprocessed_data.csv', index=False)

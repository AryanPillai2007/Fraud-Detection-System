import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest

# Load the preprocessed data
dataset = pd.read_csv('preprocessed_data.csv')

# Extract features (X) - you may select different features for unsupervised learning
X = dataset[['transaction_amount', 'transaction_time']]

# Initialize and train an Isolation Forest model for anomaly detection
isolation_forest = IsolationForest(contamination=0.05, random_state=42)
X['anomaly_score'] = isolation_forest.fit_predict(X)

# Initialize and train a DBSCAN clustering model for anomaly detection
dbscan = DBSCAN(eps=0.5, min_samples=5)
X['cluster'] = dbscan.fit_predict(X)

# Analyze the results - you can decide how to use the anomaly scores or clusters

# Save the results to a new CSV file if needed
X.to_csv('unsupervised_results.csv', index=False)

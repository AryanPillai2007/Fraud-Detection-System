import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load the integrated dataset with rule-based results
dataset = pd.read_csv('integrated_data.csv')

# Define the target variable (fraudulent vs. non-fraudulent)
y_true = dataset['fraud_label']

# Define the predictions based on your integration and rules
y_pred = dataset['rule_based_flag']

# Evaluate the system's performance
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
conf_matrix = confusion_matrix(y_true, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

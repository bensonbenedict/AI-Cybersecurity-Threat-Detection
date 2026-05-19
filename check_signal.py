import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif

df = pd.read_csv('dataset.csv')

X = df.drop('Attack Type', axis=1)
y = df['Attack Type']

# Simple label encoding for everything just to check mutual information
X_encoded = X.apply(LabelEncoder().fit_transform)
y_encoded = LabelEncoder().fit_transform(y)

mi = mutual_info_classif(X_encoded, y_encoded, random_state=42)

print("Mutual Information between features and Attack Type:")
for col, score in zip(X.columns, mi):
    print(f"{col}: {score:.4f}")

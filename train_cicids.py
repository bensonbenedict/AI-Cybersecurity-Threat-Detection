import pandas as pd
import glob
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load all CICIDS CSV files
files = glob.glob("*.csv")

df_list = []

for file in files:
    if file != "dataset.csv":
        print("Loading:", file)
        temp = pd.read_csv(file)
        df_list.append(temp)

df = pd.concat(df_list, ignore_index=True)

print("Dataset shape:", df.shape)
print(df.columns)

# Clean column names
df.columns = df.columns.str.strip()

# Replace infinity values and drop nulls
df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
df.dropna(inplace=True)
df = df.sample(n=100000, random_state=42)
print("Sampled dataset shape:", df.shape)

# Target column
print(df["Label"].value_counts())

# Convert labels: BENIGN = Normal, others = Attack
#df["Label"] = df["Label"].apply(lambda x: "Normal" if x == "BENIGN" else "Attack")

X = df.drop("Label", axis=1)
y = df["Label"]

joblib.dump(X.columns.tolist(), "feature_columns.pkl")

# Encode target
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=30,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and encoder
joblib.dump(model, "cicids_model.pkl")
joblib.dump(encoder, "cicids_label_encoder.pkl")

print("New CICIDS model saved successfully!")
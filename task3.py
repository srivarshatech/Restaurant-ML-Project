import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Dataset.csv", sep="\t")

# -----------------------------
# Data Preprocessing
# -----------------------------

# Fill missing values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# Keep only the first cuisine
df["Cuisines"] = df["Cuisines"].apply(
    lambda x: x.split(",")[0].strip()
)

# Encode target labels
encoder = LabelEncoder()
df["Cuisines"] = encoder.fit_transform(df["Cuisines"])

# Remove unnecessary columns
df = df.drop([
    "Restaurant ID",
    "Restaurant Name",
    "Address",
    "Locality",
    "Locality Verbose",
    "Rating color",
    "Rating text"
], axis=1)

# Convert categorical variables into numerical format
df = pd.get_dummies(df, drop_first=True)

# -----------------------------
# Split Features and Target
# -----------------------------
X = df.drop("Cuisines", axis=1)
y = df["Cuisines"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

precision = precision_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)

print("=" * 50)
print("Cuisine Classification")
print("=" * 50)

print(f"\nAccuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
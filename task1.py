import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Dataset.csv", sep="\t")

# -----------------------------
# Data Preprocessing
# -----------------------------

# Fill missing values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

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
X = df.drop("Aggregate rating", axis=1)
y = df["Aggregate rating"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

def main():
    ...
    
if __name__ == "__main__":
    main()

print(f"\nMean Squared Error : {mse:.4f}")
print(f"R² Score           : {r2:.4f}")

# -----------------------------
# Feature Importance
# -----------------------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features")
print("-" * 50)
print(importance.head(10))
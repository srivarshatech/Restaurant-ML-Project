import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Dataset.csv", sep="\t")

# -----------------------------
# Data Preprocessing
# -----------------------------
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# -----------------------------
# Get User Preferences
# -----------------------------
preferred_cuisine = input("Enter preferred cuisine: ")
preferred_price = int(input("Enter price range (1-4): "))

# -----------------------------
# Filter Restaurants
# -----------------------------
recommend = df[
    df["Cuisines"].str.contains(
        preferred_cuisine,
        case=False,
        na=False
    )
]

recommend = recommend[
    recommend["Price range"] == preferred_price
]

# Sort recommendations by rating
recommend = recommend.sort_values(
    by="Aggregate rating",
    ascending=False
)

# -----------------------------
# Display Results
# -----------------------------
print("=" * 50)
print("Restaurant Recommendation System")
print("=" * 50)

if recommend.empty:
    print("\nNo restaurants found matching your preferences.")
else:
    print("\nTop Recommended Restaurants:\n")
    print(
        recommend[
            [
                "Restaurant Name",
                "City",
                "Cuisines",
                "Price range",
                "Aggregate rating",
                "Votes"
            ]
        ].head(10)
    )
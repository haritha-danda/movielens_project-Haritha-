import pandas as pd
import json

df = pd.read_csv("output/top_100_movies.csv").head(10)

# Create minimal fields for dropdown
movies = []
for _, row in df.iterrows():
    movies.append({
        "title": row["title"],
        "avg_rating": round(row["avg_rating"], 2),
        "item_id": int(row["item_id"]),
        "rank": int(row["rank"]),
    })

with open("../../frontend/src/top10.json", "w") as f:
    json.dump(movies, f, indent=2)

print("top10.json generated for frontend.")

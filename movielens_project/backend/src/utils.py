import pandas as pd
import os
from typing import Tuple

def load_data(u_file: str, i_file: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    ratings = pd.read_csv(u_file, sep='\t', names=["user_id", "item_id", "rating", "timestamp"])
    movies = pd.read_csv(i_file, sep='|', encoding='latin-1', header=None, usecols=[0, 1, 5],
                         names=["item_id", "title", "genres"])
    return ratings, movies

def get_top_movies(ratings: pd.DataFrame, movies: pd.DataFrame, top_n: int = 100) -> pd.DataFrame:
    avg_ratings = ratings.groupby("item_id")["rating"].agg(["mean", "count"]).reset_index()
    avg_ratings.columns = ["item_id", "avg_rating", "num_ratings"]
    merged = avg_ratings.merge(movies, on="item_id")
    top_movies = merged.sort_values(by=["avg_rating", "num_ratings"], ascending=[False, False]).head(top_n)
    top_movies.reset_index(drop=True, inplace=True)
    top_movies["rank"] = top_movies.index + 1
    return top_movies[["rank", "item_id", "title", "avg_rating"]]

def save_csv(df: pd.DataFrame, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)

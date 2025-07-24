from src.utils import get_top_movies
import pandas as pd

def test_get_top_movies():
    ratings = pd.DataFrame({
        'item_id': [1, 1, 2, 2, 3],
        'rating': [5, 4, 3, 3, 2],
        'user_id': [10, 11, 12, 13, 14],
        'timestamp': [1, 2, 3, 4, 5]
    })
    movies = pd.DataFrame({
        'item_id': [1, 2, 3],
        'title': ['Movie A', 'Movie B', 'Movie C'],
        'genres': ['Action', 'Comedy', 'Drama']
    })
    result = get_top_movies(ratings, movies, top_n=2)
    assert len(result) == 2
    assert result.iloc[0]["title"] == "Movie A"

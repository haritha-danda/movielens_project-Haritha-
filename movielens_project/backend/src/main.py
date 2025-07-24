from utils import load_data, get_top_movies, save_csv

def main():
    ratings, movies = load_data("../data/u.data", "../data/u.item")
    top_movies = get_top_movies(ratings, movies)
    save_csv(top_movies, "output/top_100_movies.csv")

if __name__ == "__main__":
    main()

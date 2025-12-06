import pandas as pd
from movie_structs import MoviesTable

def load_movies(csv_path: str, table_size: int = 100_000) -> MoviesTable:
    movies = MoviesTable(table_size)
    df = pd.read_csv(csv_path)
    for row in df.itertuples(index=False):
        movieId = int(row.movieId)
        title = row.title
        genres = row.genres
        year = row.year

        movies.add_movie(movieId, title, genres, year)
    return movies

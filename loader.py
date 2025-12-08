import pandas as pd
from movie_structs import MoviesTable
from user_structs import UserRatingsTable
from tags_structs import TagsTable
from trie import TrieST

def load_movies(csv_path: str, table_size: int = 100_000):
    movies = MoviesTable(table_size)
    trie = TrieST()

    df = pd.read_csv(csv_path)

    for row in df.itertuples(index=False):
        movieId = int(row.movieId)
        title = row.title
        genres = row.genres
        year = None

        movies.add_movie(movieId, title, genres, year)
        trie.put(title, movieId)

    return movies, trie

def load_ratings(csv_path: str, movies: MoviesTable, users: UserRatingsTable) -> None:
    df = pd.read_csv(csv_path)
    for row in df.itertuples(index=False):
        userId = int(row.userId)
        movieId = int(row.movieId)
        rating = float(row.rating)

        movies.add_rating(movieId, rating)

        users.add_rating(userId, movieId, rating)

    movies.finalize_ratings()

def load_tags(csv_path: str, tags_table: TagsTable) -> None:
    df = pd.read_csv(csv_path)
    for row in df.itertuples(index=False):
        movieId = int(row.movieId)
        tag = str(row.tag)
        tags_table.add(tag, movieId)

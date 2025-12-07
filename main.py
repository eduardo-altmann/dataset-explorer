from loader import load_movies, load_ratings

if __name__ == "__main__":
    movies = load_movies("movies.csv")
    load_ratings("miniratings.csv", movies)

    m = movies.table.get(7)
    if m is not None:
        print(m.movieId, m.title, m.rating_avg, m.rating_count)

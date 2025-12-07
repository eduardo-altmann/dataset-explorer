from loader import load_movies, load_ratings
from user_structs import UserRatingsTable
from queries import query_top

if __name__ == "__main__":
    movies = load_movies("movies.csv")
    users = UserRatingsTable(300_000)
    load_ratings("miniratings.csv", movies, users)

    res = query_top(movies, 10, "Comedy")
    for m in res:
        print(m.movieId, m.title, m.rating_avg, m.rating_count)

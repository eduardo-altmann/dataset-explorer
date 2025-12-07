from loader import load_movies, load_ratings
from user_structs import UserRatingsTable

if __name__ == "__main__":
    movies = load_movies("movies.csv")
    users = UserRatingsTable(300_000)

    load_ratings("miniratings.csv", movies, users)

    # teste: pega as avaliações de um usuário
    ur = users.get_user_ratings(4)
    if ur:
        for r in ur[:5]:
            m = movies.table.get(r.movieId)
            print(r.movieId, r.rating, "->", m.title)

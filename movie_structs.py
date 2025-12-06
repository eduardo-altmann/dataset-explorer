from hash_table import HashTable

class Movie:
    def __init__(self, movieId, title, genres, year):
        self.movieId = movieId
        self.title = title
        self.genres = genres
        self.year = year

        self.rating_sum = 0.0
        self.rating_count = 0
        self.rating_avg = 0.0

class MoviesTable:              # eh um wrapper pra estrutura base hash table, só adaptada pros movies
    def __init__(self, size):
        self.table = HashTable(size)
    
    def add_movie(self, movieId, title, genres, year):
        movie = Movie(movieId, title, genres, year)
        self.table.insert(movieId, movie)
    
    def add_rating(self, movieId, rating):
        movie = self.table.get(movieId)
        if movie is not None:
            movie.rating_sum += rating
            movie.rating_count += 1
        
    def finalize_ratings(self):
        for _, movie in self.table.items():
            if movie.rating_count > 0:
                movie.rating_avg = movie.rating_sum / movie.rating_count

from hash_table import HashTable

class UserRating:
    def __init__(self, movieId, rating):
        self.movieId = movieId
        self.rating = rating

class UserRatingsTable:
    def __init__(self, size):
        self.table = HashTable(size)
    
    def add_rating(self, userId, movieId, rating):
        ratings_list = self.table.get(userId)

        if ratings_list is None:
            ratings_list = []
            self.table.insert(userId, ratings_list)
        
        ratings_list.append(UserRating(movieId, rating))
    
    def get_user_ratings(self, userId):
        return self.table.get(userId)

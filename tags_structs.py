from hash_table import HashTable

class TagsTable:
    def __init__(self, size):
        self.table = HashTable(size)

    def add(self, tag, movieId):
        tag_norm = tag.strip().lower()
        movies_list = self.table.get(tag_norm)
        if movies_list is None:
            movies_list = []
            self.table.insert(tag_norm, movies_list)

        if movieId not in movies_list:
            movies_list.append(movieId)
            
        movies_list.append(movieId)

    def get_movies(self, tag):
        tag_norm = tag.strip().lower()
        return self.table.get(tag_norm)

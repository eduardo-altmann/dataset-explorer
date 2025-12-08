from sort_utils import quicksort_random_hoare

def query_top(movies_table, N, genero):
    candidatos = []
    # aqui o codigo popula o array que vai ser ordenado, tem um filtro minimo de avaliacoes
    for _, movie in movies_table.table.items():
        if movie is None:
            continue

        if genero in movie.genres and movie.rating_count >= 10:         # ver depois esse numero minimo de avaliacoes
            candidatos.append(movie)
        
    if len(candidatos) == 0:
        return []
    
    quicksort_random_hoare(candidatos, 0, len(candidatos) - 1,
                           key=lambda m: m.rating_avg,
                           reverse = True)
    
    return candidatos[:N]       # retorna só os N primeiros

def query_user(movies_table, users_table, userId):
    ratings_list = users_table.get_user_ratings(userId)
    if ratings_list is None:
        return []

    resultados = []         # a diferença pro ratings_list é que lá possui só o movieId, aqui possui o nodo movie mesmo
    for ur in ratings_list:
        movie = movies_table.table.get(ur.movieId)
        if movie is None:
            continue

        resultados.append({
            "movie": movie,
            "userRating": ur.rating})

    if(len(resultados) == 0):
        return []
    
    def key_func(item):             # isso será usado no quicksort, o criterio principal vai ser o userRating, se tiver empate o de desempate é rating_avg
        return (item["userRating"], item["movie"].rating_avg)
    
    quicksort_random_hoare(
        resultados,
        0,
        len(resultados) - 1,
        key=key_func,
        reverse=True
    )

    # limita a 20
    return resultados[:20]


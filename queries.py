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

def query_tags(movies_table, tags_table, tag1, tag2):
    lista1 = tags_table.get_movies(tag1)
    lista2 = tags_table.get_movies(tag2)

    if not lista1 or not lista2:
        return []
    

    seen = set()
    for m in lista1:
        seen.add(m)

    intersecao = []
    ja_colocado = set()

    for m in lista2:
        if m in seen and m not in ja_colocado:
            intersecao.append(m)
            ja_colocado.add(m)

        
    if not intersecao:
        return []
    
    filmes = []
    
    for movieId in intersecao:
        movie = movies_table.table.get(movieId)
        if movie is not None and movie.rating_count > 0:
            filmes.append(movie)
    
    if not filmes:
        return []
    
    quicksort_random_hoare(
        filmes,
        0,
        len(filmes) - 1,
        key=lambda m: m.rating_avg,
        reverse=True
    )

    return filmes

def query_prefix(movies_table, trie, prefix):
    movieIds = trie.movie_ids_with_prefix(prefix)
    resultados = []

    for mid in movieIds:
        movie = movies_table.table.get(mid)
        if movie is not None and movie.rating_count > 0:
            resultados.append(movie)

    if not resultados:
        return []

    quicksort_random_hoare(
        resultados,
        0,
        len(resultados) - 1,
        key=lambda m: m.rating_avg,
        reverse=True
    )

    return resultados

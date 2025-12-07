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

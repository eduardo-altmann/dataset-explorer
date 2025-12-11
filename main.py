import time
from loader import load_movies, load_ratings, load_tags
from user_structs import UserRatingsTable
from tags_structs import TagsTable
from queries import query_top, query_user, query_tags, query_prefix


def parse_tags_command(line: str):
    # espera algo do tipo: tags "tag 1" "tag 2"
    partes = line.split('"')
    if len(partes) < 5:
        return None, None

    tag1 = partes[1]
    tag2 = partes[3]
    return tag1, tag2


def main():
    print("Carregando dados (fase de construção)...")

    start_time = time.time()

    # movies.csv -> MoviesTable e Trie
    movies, trie = load_movies("movies.csv")

    # ratings.csv -> atualiza MoviesTable e Users
    users = UserRatingsTable(300_000)
    load_ratings("ratings.csv", movies, users)

    # tags.csv -> TagsTable
    tags = TagsTable(200_000)
    load_tags("tags.csv", tags)

    end_time = time.time()
    build_time = end_time - start_time

    print(f"Fase de construção concluída em {build_time:.3f} segundos.")
    print("Modo console. Comandos: top, user, tags, prefix, quit.")

    while True:
        try:
            line = input(">> ").strip()
        except EOFError:
            break

        if not line:
            continue

        if line == "quit":
            break

        parts = line.split()
        cmd = parts[0]

        # top N genero
        
        if cmd == "top":
            if len(parts) < 3:
                print("Uso: top N genero")
                continue

            try:
                N = int(parts[1])
            except ValueError:
                print("N precisa ser inteiro.")
                continue

            genero = " ".join(parts[2:])

            resultados = query_top(movies, N, genero)

            if not resultados:
                print("Nenhum filme encontrado para esse gênero.")
                continue

            # movieId, title, genres, global_avg, rating_count
            for m in resultados:
                print(
                    f"{m.movieId}\t"
                    f"{m.title}\t"
                    f"{m.genres}\t"
                    f"{m.rating_avg:.6f}\t"
                    f"{m.rating_count}"
                )

        # user userId

        elif cmd == "user":
            if len(parts) < 2:
                print("Uso: user userId")
                continue

            try:
                userId = int(parts[1])
            except ValueError:
                print("userId precisa ser inteiro.")
                continue

            resultados = query_user(movies, users, userId)

            if not resultados:
                print("Nenhuma avaliação encontrada para esse usuário.")
                continue

            # movieId, title, genres, global_avg, rating_count, user_rating
            for item in resultados:
                m = item["movie"]
                ur = item["userRating"]

                print(
                    f"{m.movieId}\t"
                    f"{m.title}\t"
                    f"{m.genres}\t"
                    f"{m.rating_avg:.6f}\t"
                    f"{m.rating_count}\t"
                    f"{ur:.1f}"
                )

        # tags "tag 1" "tag 2"
        elif cmd == "tags":
            tag1, tag2 = parse_tags_command(line)

            if tag1 is None or tag2 is None:
                print('Uso: tags "tag 1" "tag 2"')
                continue

            resultados = query_tags(movies, tags, tag1, tag2)

            if not resultados:
                print("Nenhum filme encontrado com ambas as tags.")
                continue

            # movieId, title, genres, global_avg, rating_count
            for m in resultados:
                print(
                    f"{m.movieId}\t"
                    f"{m.title}\t"
                    f"{m.genres}\t"
                    f"{m.rating_avg:.6f}\t"
                    f"{m.rating_count}"
                )

        # prefix <texto>
        elif cmd == "prefix":
            if len(parts) < 2:
                print("Uso: prefix <texto>")
                continue

            # tudo depois de prefix eh o prefixo
            prefix_text = " ".join(parts[1:])

            resultados = query_prefix(movies, trie, prefix_text)

            if not resultados:
                print("Nenhum filme encontrado para esse prefixo.")
                continue

            # movieId, title, genres, global_avg, rating_count
            for m in resultados:
                print(
                    f"{m.movieId}\t"
                    f"{m.title}\t"
                    f"{m.genres}\t"
                    f"{m.rating_avg:.6f}\t"
                    f"{m.rating_count}"
                )

        else:
            print("Comando inválido.")


if __name__ == "__main__":
    main()

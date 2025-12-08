# main.py
from loader import load_movies, load_ratings, load_tags
from user_structs import UserRatingsTable
from queries import query_top, query_user, query_tags, query_prefix
from tags_structs import TagsTable

def parse_tags_command(line):
    partes = line.split('"')
    if len(partes) < 5:
        return None, None

    tag1 = partes[1]
    tag2 = partes[3]
    return tag1, tag2


def main():
    print("Carregando dados...")
    movies, trie = load_movies("movies.csv")
    users = UserRatingsTable(300_000)
    tags = TagsTable(200_000)
    load_ratings("miniratings.csv", movies, users)
    load_tags("tags.csv", tags)
    print("Pronto! Digite comandos. Ex: top 10 Comedy  | quit para sair.")

    while True:
        line = input(">> ").strip()
        if not line:
            continue
        if line == "quit":
            break

        parts = line.split()
        cmd = parts[0]

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
                print("Nenhum filme encontrado.")
                continue

            for m in resultados:
                print(f"{m.movieId}\t{m.title}\t{m.genres}\t{m.rating_avg:.4f}\t{m.rating_count}")

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

            for item in resultados:
                m = item["movie"]
                ur = item["userRating"]
                print(f"{m.movieId}\t{m.title}\t{m.genres}\t"
                      f"userRating={ur:.1f}\tglobalAvg={m.rating_avg:.4f}\tcount={m.rating_count}")
                
        elif cmd == "tags":
            tag1, tag2 = parse_tags_command(line)

            if tag1 is None or tag2 is None:
                print('Uso: tags "tag 1" "tag 2"')
                continue

            resultados = query_tags(movies, tags, tag1, tag2)

            if not resultados:
                print("Nenhum filme encontrado.")
                continue

            for m in resultados:
                print(f"{m.movieId}\t{m.title}\t{m.genres}\t{m.rating_avg:.4f}\t{m.rating_count}")
        
        elif cmd == "prefix":
            if len(parts) < 2:
                print("Uso: prefix <texto>")
                continue

            prefix_text = " ".join(parts[1:])
            resultados = query_prefix(movies, trie, prefix_text)
            if not resultados:
                print("Nenhum filme encontrado para esse prefixo.")
                continue

            for m in resultados:
                print(f"{m.movieId}\t{m.title}\t{m.genres}\t"
                      f"{m.rating_avg:.4f}\t{m.rating_count}")

        else:
            print("Comando inválido.")
        

if __name__ == "__main__":
    main()

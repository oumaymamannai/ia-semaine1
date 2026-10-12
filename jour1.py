import requests
import json

# 1. Appel HTTP GET (comme fetch en JS ou RestTemplate en Java)
reponse = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
reponse.raise_for_status()      # erreur si le statut n'est pas 2xx
posts = reponse.json()          # le JSON devient une liste de dictionnaires

# 2. Traitement : on garde les posts de l'utilisateur 1
posts_user1 = [p for p in posts if p["userId"] == 1]

# 3. Affichage
for p in posts_user1:
    print(p["id"], "-", p["title"])

# 4. Sauvegarde dans un fichier JSON
with open("posts_user1.json", "w", encoding="utf-8") as f:
    json.dump(posts_user1, f, ensure_ascii=False, indent=2)

print(f"{len(posts_user1)} posts sauvegardés")
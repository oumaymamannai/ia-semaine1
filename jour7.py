import math
import ollama

MODELE_EMBEDDING = "bge-m3"

QUESTION = "Quels sont les limites du RAG ?"

PASSAGES = [
    "RAG reduces hallucinations by grounding answers in retrieved documents.",
    "Le RAG permet de mettre à jour les connaissances sans ré-entraîner le modèle.",
    "A limitation of RAG is that answer quality depends on retrieval quality.",
    "Le restaurant universitaire ferme à 14 heures.",
    "La faculté organise les examens de fin de semestre en décembre.",
    "The cafeteria closes at 2 pm.",
]


def cosinus(a, b):
    """Similarité cosinus : proche de 1 = même sens, proche de 0 = sans rapport."""
    produit = sum(x * y for x, y in zip(a, b))
    norme_a = math.sqrt(sum(x * x for x in a))
    norme_b = math.sqrt(sum(y * y for y in b))
    return produit / (norme_a * norme_b)


# 1. Vectoriser la question et tous les passages en un seul appel
reponse = ollama.embed(model=MODELE_EMBEDDING, input=[QUESTION] + PASSAGES)
vecteurs = reponse["embeddings"]
vecteur_question = vecteurs[0]
vecteurs_passages = vecteurs[1:]

print("Taille d'un vecteur :", len(vecteur_question))
print("5 premiers nombres :", [round(x, 3) for x in vecteur_question[:5]])
print()

# 2. Mesurer la proximité de chaque passage avec la question
scores = [(cosinus(vecteur_question, v), p) for v, p in zip(vecteurs_passages, PASSAGES)]

# 3. Classer du plus proche au plus éloigné
scores.sort(reverse=True)

print("Question :", QUESTION)
for score, passage in scores:
    print(f"  {score:.3f}  {passage}")
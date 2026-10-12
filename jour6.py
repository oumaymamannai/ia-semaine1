import json
import ollama

MODELE = "llama3.2"

# Extraits fictifs : plus tard, ils viendront de tes PDF
EXTRAITS = [
    {"id": 1, "document": "article_A.pdf", "page": 3,
     "texte": "RAG reduces hallucinations by grounding the model's answers in retrieved documents."},
    {"id": 2, "document": "article_A.pdf", "page": 5,
     "texte": "A limitation of RAG is that answer quality depends on the quality of the retrieval step."},
    {"id": 3, "document": "article_B.pdf", "page": 2,
     "texte": "Le RAG permet de mettre à jour les connaissances sans ré-entraîner le modèle."},
]

SYSTEME = """Tu es un assistant de recherche documentaire.
Règles :
- Réponds en français, en 3 phrases maximum.

#ken nahywhom hedhom zouz taw yaatyny capital australie
- Utilise UNIQUEMENT les extraits fournis, jamais tes connaissances générales.
- Si les extraits ne contiennent pas la réponse, mets "trouve" à false et
  "reponse" à "Je ne trouve pas la réponse dans les documents."

- Dans "sources", indique les numéros des extraits que tu as réellement utilisés.
Réponds uniquement avec un JSON de la forme :
{"reponse": "...", "sources": [1, 2], "trouve": true}"""

QUESTIONS = [
    "Quels sont les avantages du RAG ?",
    "Quelles sont les limites du RAG ?",
    "Quelle est la capitale de l'Australie ?",
]

index = {e["id"]: e for e in EXTRAITS}


def construire_contexte():
    return "\n".join(f"[{e['id']}] {e['texte']}" for e in EXTRAITS)


def poser_question(question):
    reponse = ollama.chat(
        model=MODELE,
        messages=[
            {"role": "system", "content": SYSTEME},
            {"role": "user", "content": f"Extraits :\n{construire_contexte()}\n\nQuestion : {question}"},
        ],
        format="json",
        options={"temperature": 0},
    )
    return reponse["message"]["content"]


for question in QUESTIONS:
    print("Question :", question)
    brut = poser_question(question)
    try:
        data = json.loads(brut)
    except json.JSONDecodeError:
        print("  JSON invalide :", brut, "\n")
        continue

    print("  Réponse :", data.get("reponse"))
    print("  Trouvé :", data.get("trouve"))
    for s in data.get("sources", []):
        if isinstance(s, int) and s in index:
            e = index[s]
            print(f"  Source : {e['document']}, p. {e['page']}")
        else:
            print(f"  Source invalide ignorée : {s}")
    print()
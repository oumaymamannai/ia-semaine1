import ollama

MODELE = "llama3.2"

CONTEXTE = """Le RAG (Retrieval-Augmented Generation) est une technique qui consiste à
retrouver des passages pertinents dans des documents, puis à les fournir à un LLM
pour qu'il génère sa réponse à partir de ces sources. Cela réduit les hallucinations
et permet de répondre sur des données que le modèle n'a pas apprises."""

question = "Qu'est-ce que le RAG ?"

reponse = ollama.chat(
    model=MODELE,
    messages=[
        {"role": "system", "content": "Réponds en français, en 3 phrases maximum, UNIQUEMENT à partir du contexte fourni. Si la réponse n'y est pas, dis que tu ne sais pas."},
        {"role": "user", "content": f"Contexte :\n{CONTEXTE}\n\nQuestion : {question}"},
    ],
    options={"temperature": 0},
)

print(reponse["message"]["content"])
import ollama

MODELE = "llama3.2"

# La mémoire du chatbot : c'est NOUS qui la gardons
historique = [
    {"role": "system", "content": "Tu es un assistant pédagogique. Réponds toujours en français, de façon concise."}
]

while True:
    question = input("Vous : ")
    if question.strip().lower() == "quit":
        break
    if not question.strip():
        continue

    historique.append({"role": "user", "content": question})
    try:
        reponse = ollama.chat(
            model=MODELE,
            messages=historique,
            options={"temperature": 0.3},
        )
    except Exception as e:
        print("Erreur :", e)
        historique.pop()        # on retire la question qui a échoué
        continue

    texte = reponse["message"]["content"]
    historique.append({"role": "assistant", "content": texte})
    print("Bot :", texte)
    print("(tokens envoyés :", reponse["prompt_eval_count"], ")")
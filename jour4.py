import os
import ollama
from google import genai


MODELE = "llama3.2"
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

reponse = ollama.chat(
    model=MODELE,
    messages=[
        {"role": "system", "content": "Tu es un assistant pédagogique. Réponds en français, de façon concise."},
        {"role": "user", "content": "Explique le RAG en trois phrases."},
    ],
    options={"temperature": 0.3},
)

print(reponse["message"]["content"])
print("Tokens entrée :", reponse["prompt_eval_count"])
print("Tokens sortie :", reponse["eval_count"])
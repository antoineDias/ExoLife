from fastapi import FastAPI
import os
from dotenv import load_dotenv
import requests

load_dotenv()
# Récupère la clé d'API OpenAI à partir des variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Crée une instance de l'application FastAPI
app = FastAPI()

# Définition d'une route de base qui répond à des requêtes GET à l'URL "/"
# Un endpoint de base qui renvoie un simple JSON pour tester que l'API fonctionne
@app.get("/")
def read_root():
        # Quand cette route est appelée, elle retourne un dictionnaire JSON
    return {"Hello": "World"}

# Endpoint GET /citation qui renvoie une citation de jeu vidéo aléatoire
@app.get("/citation")
def get_zelda_citation():
    # Définit les en-têtes de la requête HTTP, y compris l'authentification via la clé d'API
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    # Corps de la requête avec les paramètres pour l'API OpenAI
    data = {
        "prompt": "Donne-moi une citation célèbre dans 'The legend of Zelda: Breath of the Wild'. Exemple: 'C'est dangereux d'aller seul! Prends ça.'",  
    }
    # Envoie la requête POST à l'API OpenAI et récupère la réponse
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", json=data, headers=headers)
    # tests
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    # Vérifie si la requête a réussi
    if response.status_code == 200:
        # Extrait la citation de la réponse JSON et la renvoie
        citation = response.json().get("choices")[0].get("text").strip()
        return {"citation": citation}
    else:
        # En cas d'échec, renvoie un message d'erreur
        return {"error": "Unable to fetch quote from OpenAI"}

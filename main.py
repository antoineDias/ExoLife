from fastapi import FastAPI

app = FastAPI()

# Définition d'une route de base qui répond à des requêtes GET à l'URL "/"
@app.get("/")
def read_root():
        # Quand cette route est appelée, elle retourne un dictionnaire JSON
    return {"Hello": "World"}
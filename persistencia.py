import json
import os

def carregar_dados():
    if os.path.exists("data.json"):
        with open("data.json", "r") as arquivo:
            return json.load(arquivo)
    return []
        
def salvar_dados(lista):
    with open("data.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)
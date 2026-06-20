# from typing import List, TypedDict
# from pydantic import BaseModel, Field

# # ==========================================
# # ESEMPIO 1: Output Strutturato con Pydantic
# # ==========================================
# # Questo è il metodo più robusto. Definisce una classe con tipi rigidi.

# class Recensione(BaseModel):
#     id_prodotto: int
#     voto: int = Field(description="Un punteggio da 1 a 5")
#     commento: str
#     sentiment: str  # es. "Positivo", "Negativo", "Neutro"
#     tag_chiave: List[str]

# # Simuliamo una stringa JSON che potrebbe arrivare da un LLM o da un'API
# json_ricevuto = """
# {
#     "id_prodotto": 9845,
#     "voto": 5,
#     "commento": "Il codice gira benissimo e l'interfaccia è intuitiva!",
#     "sentiment": "Positivo",
#     "tag_chiave": ["software", "python", "ottimo"]
# }
# """

# # Facciamo il parsing del JSON direttamente nel nostro modello strutturato
# recensione_validata = Recensione.model_validate_json(json_ricevuto)


# # ==========================================
# # ESEMPIO 2: Output Strutturato con TypedDict
# # ==========================================
# # Se non vuoi usare librerie esterne, puoi usare TypedDict (nativo da Python 3.8+)
# # per definire la struttura che un dizionario deve obbligatoriamente avere.

# class ProfiloUtente(TypedDict):
#     username: str
#     email: str
#     attivo: bool
#     badge: List[str]

# # Creazione dell'oggetto strutturato secondo il dizionario tipizzato
# utente_1: ProfiloUtente = {
#     "username": "CodeMaster26",
#     "email": "studente@bootcamp.it",
#     "attivo": True,
#     "badge": ["Primo Codice", "Fan di Python"]
# }


# # ==========================================
# # STAMPA DEI RISULTATI
# # ==========================================
# if __name__ == "__main__":
#     print("--- ESEMPIO 1: Oggetto Pydantic Validato ---")
#     print(f"Tipo di oggetto: {type(recensione_validata)}")
#     print(f"ID Prodotto: {recensione_validata.id_prodotto}")
#     print(f"Sentiment: {recensione_validata.sentiment}")
#     print(f"Tag: {recensione_validata.tag_chiave}\n")

#     print("--- ESEMPIO 2: Dizionario Strutturato (TypedDict) ---")
#     print(f"Tipo di oggetto: {type(utente_1)}")
#     print(f"Username: {utente_1['username']}")
#     print(f"Stato Attivo: {utente_1['attivo']}")





from typing import List
from pydantic import BaseModel, Field
from dataclasses import dataclass

# ==========================================
# ESEMPIO 1: Output Strutturato con Pydantic
# ==========================================
# (Rimane basato su Pydantic per la validazione stringente dei dati)

class Recensione(BaseModel):
    id_prodotto: int
    voto: int = Field(description="Un punteggio da 1 a 5")
    commento: str
    sentiment: str  # es. "Positivo", "Negativo", "Neutro"
    tag_chiave: List[str]

# Simuliamo una stringa JSON che potrebbe arrivare da un LLM o da un'API
json_ricevuto = """
{
    "id_prodotto": 9845,
    "voto": 5,
    "commento": "Il codice gira benissimo e l'interfaccia è intuitiva!",
    "sentiment": "Positivo",
    "tag_chiave": ["software", "python", "ottimo"]
}
"""

# Facciamo il parsing del JSON direttamente nel nostro modello strutturato
recensione_validata = Recensione.model_validate_json(json_ricevuto)


# ==========================================
# ESEMPIO 2: Output Strutturato con Dataclass (Nuovo)
# ==========================================
# Le dataclass sono native in Python. A differenza di TypedDict (che crea un dizionario),
# la dataclass crea un vero e proprio OGGETTO i cui attributi sono accessibili con il punto (.).

@dataclass
class ProfiloUtente:
    username: str
    email: str
    attivo: bool
    badge: List[str]

# Creazione dell'oggetto strutturato usando la Dataclass
# Noterai che lo istanziamo come una classe, non come un dizionario con le graffe!
utente_1 = ProfiloUtente(
    username="CodeMaster26",
    email="studente@bootcamp.it",
    attivo=True,
    badge=["Primo Codice", "Fan di Python"]
)


# ==========================================
# STAMPA DEI RISULTATI
# ==========================================
if __name__ == "__main__":
    print("--- ESEMPIO 1: Oggetto Pydantic Validato ---")
    print(f"Tipo di oggetto: {type(recensione_validata)}")
    print(f"ID Prodotto: {recensione_validata.id_prodotto}")
    print(f"Sentiment: {recensione_validata.sentiment}\n")

    print("--- ESEMPIO 2: Oggetto Strutturato (Dataclass) ---")
    print(f"Tipo di oggetto: {type(utente_1)}")
    # Noterai che ora usiamo utente_1.username invece di utente_1['username']
    print(f"Username: {utente_1.username}")
    print(f"Stato Attivo: {utente_1.attivo}")
    print(f"Badge: {utente_1.badge}")
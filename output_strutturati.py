import os
from typing import List, TypedDict
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key=OPENAI_KEY)


class RecensioneServizioCloud(BaseModel):
    id_infrastruttura: int
    voto: int = Field(description="Un punteggio da 1 a 5 basato sulla qualità del servizio cloud")
    commento: str
    sentiment: str = Field(description="Il sentiment estratto: 'Positivo', 'Negativo' oppure 'Neutro'")
    tag_chiave: List[str] = Field(description="Lista di tag tecnologici chiave estratti dal testo (es. cloud, server, latency)")


commento_reale_utente = """
L'infrastruttura virtuale con ID 9845 sta rispondendo benissimo. Abbiamo migrato i database 
ieri e la latenza è bassissima, i server erogano potenza senza interruzioni. Ottimo servizio cloud!
"""

def analizza_recensione_con_llm(testo_input: str) -> RecensioneServizioCloud:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer",
                "content": "Sei un analista dati IA per Nexis Cloud. Il tuo compito è analizzare i feedback testuali degli utenti sull'infrastruttura, estrarre il sentiment, assegnare un voto coerente da 1 a 5, trovare l'ID della risorsa citata e generare i tag tecnologici corretti."
            },
            {
                "role": "user",
                "content": testo_input
            }
        ],
        response_format=RecensioneServizioCloud,
    )
    return completion.choices[0].message.parsed


recensione_validata = analizza_recensione_con_llm(commento_reale_utente)



class ProfiloUtenteNexis(TypedDict):
    username: str
    email: str
    attivo: bool
    certificazioni: List[str]

utente_1: ProfiloUtenteNexis = {
    "username": "CloudArchitect26",
    "email": "sysadmin@nexiscloud.com",
    "attivo": True,
    "certificazioni": ["Nexis Cloud Advanced", "Python Cloud Automation"]
}


if __name__ == "__main__":
    print("--- ESEMPIO 1: Oggetto Pydantic Validato tramite LLM OpenAI ---")
    print(f"Tipo di oggetto generato: {type(recensione_validata)}")
    print(f"ID Infrastruttura estratto: {recensione_validata.id_infrastruttura}")
    print(f"Voto assegnato dall'AI: {recensione_validata.voto}/5")
    print(f"Sentiment Analizzato: {recensione_validata.sentiment}")
    print(f"Tag IT estratti: {recensione_validata.tag_chiave}\n")

    print("--- ESEMPIO 2: Dizionario Strutturato Aziendale (TypedDict) ---")
    print(f"Tipo di oggetto: {type(utente_1)}")
    print(f"Username: {utente_1['username']}")
    print(f"Stato Account: {'Attivo' if utente_1['attivo'] else 'Inattivo'}")
    print(f"Certificazioni Nexis: {utente_1['certificazioni']}")



# #esercizio 2
# import os
# from typing import List
# from pydantic import BaseModel, Field
# from dataclasses import dataclass
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()
# OPENAI_KEY = os.getenv('OPENAI_KEY')
# client = OpenAI(api_key=OPENAI_KEY)


# # 1. Schema dei dati per l'analisi dei ticket/recensioni di Nexis Cloud
# class AnalisiSegnalazioneCloud(BaseModel):
#     id_prodotto: int = Field(description="L'ID numerico della risorsa cloud o del servizio")
#     voto: int = Field(description="Un punteggio di soddisfazione da 1 a 5 basato sul testo")
#     commento: str = Field(description="Il riassunto o il testo della segnalazione")
#     sentiment: str = Field(description="Il sentiment estratto dal testo: 'Positivo', 'Negativo' o 'Neutro'")
#     tag_chiave: List[str] = Field(description="I tag IT estratti (es. kubernetes, migration, backup)")


# segnalazione_reale = """
# Abbiamo attivato lo storage cloud ieri (ID servizio: 7741). Devo dire che la velocità di replica 
# dei dati è fantastica, ma l'interfaccia della console ci ha messo un po' a sincronizzarsi all'inizio. 
# Nel complesso direi un ottimo 4 su 5, siamo molto soddisfatti del backup automatico.
# """


# def analizza_segnalazione_con_ai(testo_input: str) -> AnalisiSegnalazioneCloud:
#     completion = client.beta.chat.completions.parse(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "developer",
#                 "content": "Sei un sistema di monitoraggio IA per Nexis Cloud. Analizza il feedback tecnico dell'utente ed estrai le informazioni strutturate richieste dal formato."
#             },
#             {
#                 "role": "user",
#                 "content": testo_input
#             }
#         ],
#         response_format=AnalisiSegnalazioneCloud  # Forza OpenAI a rispondere con la struttura Pydantic
#     )
#     return completion.choices[0].message.parsed


# # Eseguiamo la vera chiamata LLM
# recensione_validata = analizza_segnalazione_con_ai(segnalazione_reale)


# # 2. Utilizzo della Dataclass nativa di Python per i profili dei sistemisti Nexis Cloud
# @dataclass
# class ProfiloUtente:
#     username: str
#     email: str
#     attivo: bool
#     badge: List[str]


# # Corretto l'errore di sintassi qui (tolte le virgolette e usati i corretti argomenti nominali)
# utente_1 = ProfiloUtente(
#     username="NexisCloudArchitect",
#     email="architect@nexiscloud.com",
#     attivo=True,
#     badge=["Cloud Deployer", "Python Automation Expert"]
# )


# if __name__ == "__main__":
#     print("--- ESEMPIO 1: Oggetto Pydantic Validato tramite LLM OpenAI ---")
#     print(f"Tipo di oggetto generato dall'AI: {type(recensione_validata)}")
#     print(f"ID Risorsa Cloud Estratto: {recensione_validata.id_prodotto}")
#     print(f"Voto calcolato dall'AI: {recensione_validata.voto}")
#     print(f"Sentiment Analizzato: {recensione_validata.sentiment}")
#     print(f"Tag IT rilevati: {recensione_validata.tag_chiave}\n")

#     print("--- ESEMPIO 2: Oggetto Strutturato Standard (Dataclass) ---")
#     print(f"Tipo di oggetto: {type(utente_1)}")
#     print(f"Username Profilo: {utente_1.username}")
#     print(f"Stato Account Attivo: {utente_1.attivo}")
#     print(f"Badge Aziendali: {utente_1.badge}")

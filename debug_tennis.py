#!/usr/bin/env python3
"""
Test API Tennis RapidAPI – live_scores
"""

import os, json, logging, requests

API_KEY = os.environ["RAPIDAPI_KEY"]

url = "https://ultimate-tennis1.p.rapidapi.com/live_scores"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "ultimate-tennis1.p.rapidapi.com"
}
# Se l'endpoint richiede parametri (es. date, tournament_id), aggiungili qui
params = {}   # modifica se necessario

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
try:
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    logging.info(f"Status code: {resp.status_code}")
    logging.info(f"Response text (primi 1500 caratteri): {resp.text[:1500]}")
    if resp.status_code == 200:
        data = resp.json()
        if isinstance(data, list):
            logging.info(f"Trovati {len(data)} eventi live")
            # Mostra il primo evento per vedere la struttura
            if len(data) > 0:
                logging.info(f"Primo evento: {json.dumps(data[0], indent=2)[:1000]}")
        else:
            logging.info(f"Risposta (primi 1000 caratteri): {json.dumps(data)[:1000]}")
    else:
        logging.error("Richiesta fallita")
except Exception as e:
    logging.error(f"Errore: {e}")

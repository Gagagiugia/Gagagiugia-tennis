#!/usr/bin/env python3
"""
Test API Tennis RapidAPI – debug migliorato
"""

import os, json, logging, requests

API_KEY = os.environ["RAPIDAPI_KEY"]

# Prima prova: classifica ATP (sicuramente esistente)
url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/ranking/atp/top"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "tennis-api-atp-wta-itf.p.rapidapi.com"
}
params = {}  # senza parametri

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
try:
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    logging.info(f"Status code: {resp.status_code}")
    logging.info(f"Response text (primi 500 caratteri): {resp.text[:500]}")
    if resp.status_code == 200:
        data = resp.json()
        logging.info(f"Trovati {len(data)} elementi nella classifica")
    else:
        logging.error("Richiesta fallita")
except Exception as e:
    logging.error(f"Errore: {e}")

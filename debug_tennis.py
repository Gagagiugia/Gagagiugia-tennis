#!/usr/bin/env python3
"""
Test API Tennis RapidAPI – programma giornaliero ATP
"""

import os, json, logging, requests

API_KEY = os.environ["RAPIDAPI_KEY"]

# Endpoint del programma giornaliero per un torneo ATP (ID 580 è un esempio)
# Proviamo a vedere se restituisce le partite di oggi
url = "https://ultimate-tennis1.p.rapidapi.com/atp/tournament_daily_schedule/580"
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "ultimate-tennis1.p.rapidapi.com"
}
params = {"date": "2026-08-04"}   # oggi

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
try:
    resp = requests.get(url, headers=headers, params=params, timeout=15)
    data = resp.json()
    logging.info(f"Risposta API (primi 1000 caratteri): {json.dumps(data)[:1000]}")
except Exception as e:
    logging.error(f"Errore: {e}")

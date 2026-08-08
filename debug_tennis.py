#!/usr/bin/env python3
"""
Test API OddsFeed – Tennis events
"""

import os, json, logging, requests

API_KEY = os.environ["RAPIDAPI_KEY"]

# 1. Elenco sport: cerchiamo l'ID del tennis
url_sports = "https://odds-feed.p.rapidapi.com/api/v1/sports"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "odds-feed.p.rapidapi.com"
}

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

try:
    resp = requests.get(url_sports, headers=headers, timeout=15)
    if resp.status_code == 200:
        sports = resp.json()
        tennis = next((s for s in sports if s["name"].lower() == "tennis"), None)
        if tennis:
            logging.info(f"Tennis ID: {tennis['id']} - {tennis['name']}")
            sport_id = tennis["id"]
        else:
            logging.error("Tennis non trovato tra gli sport")
            exit()
    else:
        logging.error(f"Errore HTTP {resp.status_code}: {resp.text}")
        exit()

    # 2. Eventi di tennis in programma (SCHEDULED) per oggi
    url_events = "https://odds-feed.p.rapidapi.com/api/v1/events"
    params = {
        "sport_id": sport_id,
        "status": "SCHEDULED",   # partite non ancora iniziate
        "page": 0
    }
    resp = requests.get(url_events, headers=headers, params=params, timeout=15)
    if resp.status_code == 200:
        data = resp.json()
        events = data.get("data", [])
        logging.info(f"Trovati {len(events)} eventi SCHEDULED di tennis oggi")
        # Mostriamo i primi 3 per vedere la struttura
        for ev in events[:3]:
            logging.info(f"  {ev['tournament']['name']}: {ev['team_home']['name']} vs {ev['team_away']['name']} "
                         f"| Quote: {ev.get('main_outcome_0')}/{ev.get('main_outcome_1')}/{ev.get('main_outcome_2')}")
    else:
        logging.error(f"Errore eventi: {resp.status_code} {resp.text}")

except Exception as e:
    logging.error(f"Errore: {e}")

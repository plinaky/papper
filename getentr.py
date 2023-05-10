#!/usr/bin/python3

import xml.etree.ElementTree as ET
import os, sys
import requests
import json
import sqlite3

conn = sqlite3.connect('entr.db')
url = "https://api.pappers.fr/v2/entreprise"

params = {
    "api_token": "201cdf0203b09bbdad02e742ecb5c1692a0f218daa484485",
    "siren": "552030967",
    "format_publications_bodacc": "objet",
    "marques": True,
    "validite_tva_intracommunautaire": True,
    "publications_bodacc_brutes": False
}

reponse = requests.get(url, params)

if reponse.status_code == 200 :
    print('reponse complete')
    print('******************************')
    myjson = json.loads(reponse.text)
    print(json.dumps(myjson, sort_keys=False, indent=4))
elif reponse.status_code == 206:
    print('reponse incomplete')
    print('******************************')
    myjson = json.loads(reponse.test)
    print(json.dumps(myjson, sort_keys=False, indent=4))
elif reponse.status_code == 400:
    print('Parametres de la requete incorrects')
elif reponse.status_code == 401:
    print('Cle API incorrecte')
elif reponse.status_code == 404:
    print('Association inexistante')
elif reponse.status_code == 503:
    print('503 Service momentanement indisponible')
else :
    print("code d'erreur inconnu", reponse.status_code)


db.close()

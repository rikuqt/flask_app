import json
import requests

mittaus = {"x": 6,
           "y": 10}

while(True):
    mittaus["x"] = int(input("Anna viikonpäivän numero >"))
    mittaus["y"] = int(input("Anna päivän lämpötila >"))

    viesti = json.dumps(mittaus)
    vastaus = requests.post('http://localhost:5000/lisaakantaan', data=viesti)
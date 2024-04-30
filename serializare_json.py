'''
JSON : JavaScript Object Notation

API : application programming interface
expui metode/clase/variabile catre cineva
endpoint: URL
comunicare/transfer informatii: JSON

standardul REST
get
set
'''

import json

with open("fisier.json") as file:
    data = json.load(file)

print(data["haine"][0])
import json

with open("fisier.json") as file:
    data = json.load(file)

print(data["haine"][0])
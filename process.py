import json
from pprint import pprint

with open('C:\Users\David\Documents\GitHub\\fbData\convo') as jsonData:
    d = json.load(jsonData)
    jsonData.close()


print d['peeps']

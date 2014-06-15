import json
from pprint import pprint

with open('c:\users\david\downloads\download (2)') as jsonData:
    d = json.load(jsonData)
    jsonData.close()
    pprint(d)

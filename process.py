import json
from pprint import pprint

with open('C:\Users\David\Documents\GitHub\\fbData\convo') as jsonData:
    d = json.load(jsonData)
    jsonData.close()

#userList stucture:
# {
#   u1 : {
#           words : [[num]],
#           messages : [[num]]
#       }
#
userList = {}

for m in d['messages']:
    numWords = len(m['text'].split(" "))
    if m['user'] not in userList.keys():
        userList[m['user']]={'words':numWords, 'messages':1}
    else:
        userList[m['user']]['words'] += numWords
        userList[m['user']]['messages'] += 1

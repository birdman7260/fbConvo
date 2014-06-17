import json
import sys, nltk
import datetime
from pprint import pprint

#see wordHistogram
histoString = ''

#see timeLine
dateDict = {}

#see hourHistogram
hourDict = {}

#escape the f, a.k.a get the f outta there!
with open('C:\Users\David\Documents\GitHub\\fbData\chelConvo') as jsonData:
    d = json.load(jsonData)

#userList stucture:
# {
#   u1 : {
#           words : [[num]],
#           messages : [[num]]
#       }
#
userList = {}

def wordCount():
    f = open('wordDump.txt','w')
    for m in d['messages']:
        #add the raw string of the message to the wordDump for wordl
        try:
            f.write(m['text']+'\n')
        except UnicodeEncodeError:
            #print 'unable to encode '+m['text']
            pass
        
        #tokenize the message content
        numWords = len(m['text'].split(" "))

        #if user isn't already there, add and initialize. otherwise, add to his sum
        if m['user'] not in userList.keys():
            userList[m['user']]={'words':numWords, 'messages':1}
        else:
            userList[m['user']]['words'] += numWords
            userList[m['user']]['messages'] += 1

def timeLine():
    fl = open('timeLine.csv','w')
    msgs = iter(d['messages'])
    try:
        m = msgs.next()
        while True:
            wordCount = 0
            date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            temp = date
            while temp.date() == date.date():
                wordCount += len(m['text'].split(" "))
                m = msgs.next()
                temp = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S.%fZ')

            dateDict[str(date.date())] = wordCount
            fl.write(str(date.date())+','+str(wordCount)+'\n')
    except StopIteration:
        print("No more messages.")
        fl.close()

#need to -5hrs from GMT
def hourHistogram():
    for m in d['messages']:
        date = datetime.datetime.strptime(m['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        if date.hour not in hourDict.keys():
            hourDict[date.hour] = 1
        else:
            hourDict[date.hour] += 1
        
def wordHistogram():
    f2 = open('wordDump.txt', 'rU')
    txt = f2.read()
    f2.close()

    tokens = nltk.word_tokenize(txt) # tokenize text
    clean_tokens = []

    for word in tokens:
        word = word.lower()
        if word.isalpha(): # drop all non-words
            clean_tokens.append(word)

    # make frequency distribution of words
    fd = nltk.FreqDist(clean_tokens)
    for token in fd:
        histoString += token + ':' + fd[token] + '\n'
        #print token, ':', fd[token]

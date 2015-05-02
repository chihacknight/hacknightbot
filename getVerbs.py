import requests
import json
import csv

url = 'http://watchout4snakes.com/wo4snakes/Random'

def getVerbs():
    data = {'Level': 20, 'Pos': 't'}
    words = []
    while len(words) < 100:
        r = requests.post('{0}/RandomWordPlus'.format(url), data=data)
        if r.content.decode('utf-8').endswith('ing'):
            words.append(r.content.decode('utf-8'))
            print('got a word: %s' % r.content)
    with open('verbs.json', 'w') as f:
        f.write(json.dumps(words))

def getNounPhrases():
    data = {
        'Level1': 20, 
        'Pos1': 'a',
        'Level2': 20,
        'Pos2': 'n',
    }
    words = []
    while len(words) < 100:
        r = requests.post('{0}/RandomPhrase'.format(url), data=data)
        words.append(r.content.decode('utf-8'))
        print('got a word: %s' % r.content)
    with open('noun_phrases.json', 'a') as f:
        f.write(json.dumps(words))

def getAgencies():
    agencies = []
    with open('USGOV.csv', 'r') as f:
        reader = csv.reader(f)
        agencies = [r[0] for r in reader]
    with open('agencies.json', 'w') as f:
        f.write(json.dumps(agencies))

def getOrgs():
    orgs = []
    with open('NONPROFITS.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        orgs = [o[1] for o in reader]
    with open('orgs.json', 'w') as f:
        f.write(json.dumps(orgs))

if __name__ == "__main__":
    # getVerbs()
    # getNounPhrases()
    getAgencies()
    getOrgs()

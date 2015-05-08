import os
import requests
import websocket
import json
import random

SLACK_AUTH_TOKEN = os.environ['SLACK_AUTH_TOKEN']
SLACK_REALTIME_ENDPOINT = 'https://slack.com/api/rtm.start'

def generateDataProject():
    madlib = 'You could use {dataset_name} ({dataset_link}) to get a better understanding of {service}'
    random_resource = random.choice(json.load(open('json_data/resources.json')))
    params = {
        'dataset_name': random_resource['title'],
        'dataset_link': random_resource['url'],
        'service': random.choice(json.load(open('json_data/services.json'))),
    }
    return madlib.format_map(params)

def generateAppIdea():
    madlib = 'An app for {verb} the {noun_phrase} of the {agency} & the {org}'
    params = {
        'verb': random.choice(json.load(open('json_data/verbs.json'))),
        'noun_phrase': random.choice(json.load(open('json_data/noun_phrases.json'))),
        'agency': random.choice(json.load(open('json_data/agencies.json'))),
        'org': random.choice(json.load(open('json_data/orgs.json')))
    }
    return madlib.format_map(params)

if __name__ == "__main__":
    params = {'token': SLACK_AUTH_TOKEN}
    socket = requests.get(SLACK_REALTIME_ENDPOINT, params=params)
    
    channel_lookup = {c['id']: c['name'] for c in socket.json()['channels']}
    user_lookup = {u['id']: u['name'] for u in socket.json()['users']}

    ws = websocket.WebSocket()
    ws.connect(socket.json()['url'])

    while True:
        result = json.loads(ws.recv())
        message_id = 1
        if result.get('type') == 'message' and not result.get('subtype'):
            channel_name = channel_lookup.get(result['channel'], 'general')
            user_name = user_lookup.get(result['user'], '')
            formatted = None
            if 'app me' in result['text'].lower():
                message = generateAppIdea()
                formatted = "Here's an idea, {0} \n {1}".format(user_name, message)

            if 'data project' in result['text'].lower():
                message = generateDataProject()
                formatted = "Here's an idea, {0} \n {1}".format(user_name, message)
            if formatted:
                postback = {
                    'id': message_id,
                    'type': 'message',
                    'channel': result['channel'],
                    'text': formatted,
                }
                ws.send(json.dumps(postback))
                message_id += 1


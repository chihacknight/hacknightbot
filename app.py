import os
import requests
import slack
import slack.chat
import websocket
import json
import random

SLACK_API_KEY = os.environ['SLACK_API_KEY']
SLACK_AUTH_TOKEN = os.environ['SLACK_AUTH_TOKEN']
SLACK_REALTIME_ENDPOINT = 'https://slack.com/api/rtm.start'

def generateAppIdea():
    madlib = 'An app for {verb} the {noun_phrase} of the {agency} & the {org}'
    params = {
        'verb': random.choice(json.load(open('verbs.json'))),
        'noun_phrase': random.choice(json.load(open('noun_phrases.json'))),
        'agency': random.choice(json.load(open('agencies.json'))),
        'org': random.choice(json.load(open('orgs.json')))
    }
    return madlib.format_map(params)

if __name__ == "__main__":
    params = {'token': SLACK_AUTH_TOKEN}
    socket = requests.get(SLACK_REALTIME_ENDPOINT, params=params)
    
    channel_lookup = {c['id']: c['name'] for c in socket.json()['channels']}
    user_lookup = {u['id']: u['name'] for u in socket.json()['users']}

    ws = websocket.WebSocket()
    ws.connect(socket.json()['url'])

    slack.api_token = SLACK_API_KEY

    while True:
        result = json.loads(ws.recv())
        if result['type'] == 'message' and not result.get('subtype'):
            channel_name = channel_lookup[result['channel']]
            user_name = user_lookup[result['user']]
            if 'app me' in result['text'].lower():
                message = generateAppIdea()
                slack.chat.post_message('#%s' % channel_name, 
                                        "Here's an idea, {0} \n {1}".format(user_name, message), 
                                        username='hack_night_bot')


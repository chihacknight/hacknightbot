# HackNightBot

A Slack bot to generate amazing ideas.

### Run it locally

You need two kinds of keys from Slack: the API key for a bot user and an Auth
token for the team that you're wanting to post the amazing ideas into.

**To get an API Key**

1. Login to your Slack team at {subdomain}.slack.com and click the settings
thing in the upper left (it'll have your team's name on it) and then click
"Configure Integrations".
2. Scroll down and find the "Bots" integration. Click "Add".
3. Give your bot a name, etc and then grab the API Key.

**To get an auth token**

1. Go here: [https://api.slack.com/web](https://api.slack.com/web), scroll down
to the bottom and find the list of teams that you belong to.
2. Click the button to issue a token for the team that you want to put your bot
in and grab the token.

**Run the app**

This app was developed using Python 3.4.3 but I'm pretty sure it'll work in
Python 2.7.x as well. Either way, get yourself a virtual enviromnent and
install the requirements: 

``` bash
# Using vanilla virtualenv 
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# Using virtualenvwrapper
$ mkvirtualenv bot
$ pip install -r requirements.txt
```

In order for the app to run, it needs the API key and auth token that you just
got set as environmental variables. So, before you can run it, you'll need to
set those:

``` bash
$ export SLACK_API_KEY='theapikey'
$ export SLACK_AUTH_TOKEN='theauthtoken'
```

To make those stick around between terminal sessions, you can add those lines
into your ``.bashrc`` file (or similar) and ``source`` it:

``` bash 
$ vim ~/.bashrc # add those to export statements
$ source ~/.bashrc
```

Now that all that is setup, you can run the app by doing ``python app.py`` with
your virtualenv activated.

### Modifying data sources

In the script called ``getMaterials.py`` there are a few functions that
generate all of the various bits and pieces that the app uses to fill in the
MadLibs that are used to create the messages. Those functions generate the JSON
files that are in ``json_data`` and which the app reads to do it's magic. If
you want to modify what the bot is saying, you can either modify the functions
that generate the JSON files or just modify the JSON files directly.

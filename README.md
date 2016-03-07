# HackNightBot

A [Slack bot](https://api.slack.com/bot-users) for [Chi Hack Night](http://chihacknight.org/). 

### Current functions

@hacknightbot hangs out in the #chihacknight channel and chimes in under one of the following conditions

* anyone types `app me` - responds with a randomized silly app idea in the form of "An app for {verb} the {noun_phrase} of the {agency} & the {org}" - by @evz
* anyone types `data project` - responds with a randomized silly data project idea in the form of "You could use {dataset_name} ({dataset_link}) to get a better understanding of {service}" - by @evz
* anyone types some form of 'hey guys' - suggests a random gender neutral alternative to address a group - by @cathydeng
* _coming soon_ welcome messages to new users - by @hunterowens, @derekeder

Add your own @hacknightbot responses by editing `app.py`!

### Run it locally

You need to get an Auth token for the team that you're wanting to post the
amazing ideas into.

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

In order for the app to run, it needs the auth token that you just got set as
an environmental variable. So, before you can run it, you'll need to set it:

``` bash
$ export SLACK_AUTH_TOKEN='theauthtoken'
```

To make those stick around between terminal sessions, you can add that line
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

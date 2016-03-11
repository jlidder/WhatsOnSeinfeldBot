import requests

def send_simple_message(twitter_text):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxWTVIDTHEYPROVIDEYOU.mailgun.org/messages",
        auth=("api", ""),
        data={"from": "Mailgun Sandbox <postmaster@sandboxWTVIDTHEYPROVIDEYOU.mailgun.org>",
              "to": "Whomever <wtv@wtv.com>, Whomever2 <wtv2@wtv2.com>",
              "subject": "On #Seinfeld tonight",
              "text": twitter_text})

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json

#Twitter Dev Tokens
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(
auth=oauth)

results = twitter.statuses.user_timeline(screen_name="SeinfeldTV")

for status in results:
    if "#Seinfeld tonight" in status["text"].encode("ascii", "ignore"):
        print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
        send_simple_message(status["text"].encode("ascii", "ignore"))
        break

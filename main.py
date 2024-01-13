# Import necessary dependencies
import tweepy
from secret import credentials

# Log into API
auth = tweepy.OAuth1UserHandler(
    credentials["API_KEY"],
    credentials["API_KEY_SECRET"],
    credentials["ACCESS_TOKEN"],
    credentials["ACCESS_TOKEN_SECRET"]
)
api = tweepy.API(auth)
client = tweepy.Client(
    credentials["BEARER_TOKEN"],
    credentials["API_KEY"],
    credentials["API_KEY_SECRET"],
    credentials["ACCESS_TOKEN"],
    credentials["ACCESS_TOKEN_SECRET"]
)

def tweet():
    # Create tweet
    client.create_tweet(text="...still love space")

tweet()
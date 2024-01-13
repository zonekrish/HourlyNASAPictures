# Import necessary dependencies
import tweepy
import requests
from bs4 import BeautifulSoup
from secret import credentials

# Assign URL to scrape
url = "https://apod.nasa.gov/apod/archivepixFull.html"

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
    # Get HTML page
    response = requests.get(url)

    # Parse page
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all elements w/ image
    elements = soup.find_all("a")

    # Print all elements
    for i in range(len(elements)):
        print(elements[i])

    # Create tweet
    # client.create_tweet(text="...still love space")

tweet()
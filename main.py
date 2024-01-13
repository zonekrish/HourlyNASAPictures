# Import necessary dependencies
import tweepy
import requests
import random
import os
import sys
from bs4 import BeautifulSoup
from secret import credentials

def tweet():
    # Remove image
    try:
        os.remove("temp.jpg")
    except:
        pass

    # Assign URL root to scrape
    url = "https://apod.nasa.gov/apod/"

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
    
    # Scrape main HTML page
    response = requests.get(url + "archivepixFull.html")
    soup1 = BeautifulSoup(response.text, "html.parser")

    # Get all elements w/ image link
    elements = soup1.find_all("a")

    # Get random number for posting image
    rand = random.randint(0, len(elements)-1)

    # Scrape page with image link
    imgResp = requests.get(url + elements[rand].get("href"))
    soup2 = BeautifulSoup(imgResp.text, "html.parser")

    # Get image page link
    imgElem = soup2.find_all("a")
    link = url + imgElem[1].get("href")

    # Download image from link
    imgData = requests.get(link).content

    with open("temp.jpg", "wb") as f:
        f.write(imgData)
    
    # Set up image metadata
    metadata = soup2.title.string
    print(metadata.strip())

    # Upload photo to Twitter
    img = api.simple_upload("temp.jpg")
    api.create_media_metadata(img.media_id, alt_text=metadata[7:])

    post = client.create_tweet(media_ids=[img.media_id])

# Check if user specified scheduled Tweets
def checkArgs():
    for i in range(len(sys.argv)):
        if (sys.argv[i] == "schedule"):
            return True
    
    return False

if (checkArgs()):
    import schedule
    import time

    schedule.every().hour.at(":00").do(tweet)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    tweet()
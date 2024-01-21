# Import necessary dependencies
import tweepy
import requests
import random
import os
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
from secret import credentials, filename

def tweet():
    # Remove image
    try:
        os.remove(filename)
    except:
        pass

    # Initialize database
    db = TinyDB("db.json")

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

    # Check if image found will be good to post
    nopost = True
    while (nopost):
        # Get random number for posting image
        rand = random.randint(0, len(elements)-11)

        # Get href for image link
        href = elements[rand].get("href")

        # Find it in database
        if (db.get(Query().href == href) != None):
            continue
        
        # Scrape page with image link
        imgResp = requests.get(url + href)
        soup2 = BeautifulSoup(imgResp.text, "html.parser")
        
        # Get image page link
        imgElem = soup2.find_all("a")

        # Get new page if current page is not photo
        if ("jpg" in imgElem[1].get("href")):
            link = url + imgElem[1].get("href")
            nopost = False

    # Download image from link
    imgData = requests.get(link).content
    with open(filename, "wb") as f:
        f.write(imgData)
    
    # Set up image metadata
    metadata = soup2.title.string.strip()
    print(metadata)

    # Upload photo to Twitter
    img = api.simple_upload(filename)
    api.create_media_metadata(img.media_id, alt_text=metadata[6:])
    post = client.create_tweet(media_ids=[img.media_id])

    # Insert image info. into databse
    db.insert({"href": href, "alt": metadata})

tweet()
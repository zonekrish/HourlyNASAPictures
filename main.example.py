# Here is the main program without posting to Twitter
# You can use this without any credentials to just see some cool photos!
import requests
import random
import os
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def getPicture():
    # Change this with the filename of your choice
    filename = "temp.jpg"

    try:
        os.remove(filename)
    except:
        pass

    db = TinyDB("db.json")

    url = "https://apod.nasa.gov/apod/"

    response = requests.get(url + "archivepixFull.html")
    soup1 = BeautifulSoup(response.text, "html.parser")

    elements = soup1.find_all("a")

    rand = random.randint(0, len(elements)-11)

    nopost = True
    while (nopost):
        href = elements[rand].get("href")

        find = Query()
        if (len(db.search(find.href == href)) < 1):
            nopost = False
        else:
            rand = random.randint(0, len(elements)-11)
            continue
    
        imgResp = requests.get(url + href)
        soup2 = BeautifulSoup(imgResp.text, "html.parser")
        
        imgElem = soup2.find_all("a")

        if ("jpg" in imgElem[1].get("href")):
            link = url + imgElem[1].get("href")
        else:
            rand = random.randint(0, len(elements)-11)
            nopost = True

    imgData = requests.get(link).content

    with open(filename, "wb") as f:
        f.write(imgData)
    
    metadata = soup2.title.string.strip()
    print(metadata)

    db.insert({"href": href, "alt": metadata})


getPicture()
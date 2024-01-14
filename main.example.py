# Here is the main program without posting to Twitter
# You can use this without any credentials to just see some cool photos!

import requests
import random
import os
from bs4 import BeautifulSoup

def getPicture():
    # Change this with the filename of your choice
    filename = "temp.jpg"

    try:
        os.remove(filename)
    except:
        pass

    url = "https://apod.nasa.gov/apod/"

    response = requests.get(url + "archivepixFull.html")
    soup1 = BeautifulSoup(response.text, "html.parser")

    elements = soup1.find_all("a")

    rand = random.randint(0, len(elements)-1)

    imgResp = requests.get(url + elements[rand].get("href"))
    soup2 = BeautifulSoup(imgResp.text, "html.parser")

    imgElem = soup2.find_all("a")
    link = url + imgElem[1].get("href")

    imgData = requests.get(link).content

    with open(filename, "wb") as f:
        f.write(imgData)
    
    metadata = soup2.title.string
    print(metadata.strip())


getPicture()
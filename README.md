# HourlyNASAPictures
A simple Python script that takes one random picture from [NASA's Astronomy Picture of the Day archive](https://apod.nasa.gov/) and posts it to Twitter. This is currently used for [@NasaPhotosBot](https://twitter.com/NasaPhotosBot).

## Usage
### Dependencies
- Python 3.* (Tested with 3.11-12)
- [tweepy](https://pypi.org/project/tweepy/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)

Make sure to have a [Twitter developer account](https://developer.twitter.com) with read + write permissions. The free tier works fine, and remember to set your bot account to "Automated" to avoid getting banned!

### Set-up
1. Clone the repository to any working directory
2. In the directory, run `pip install -r requirements.txt` to install the needed dependencies
3. Create any needed directory for storing the pictures
4. Add your Twitter API credentials and picture directory inside of `secret.example.py`, rename this to `secret.py` when done.
5. Run `main.py` manually or use a scheduling service such as cron to automate Tweets

### Syntax
To post a picture onto Twitter:
> python main.py

To get a picture onto your directory (no posting to Twitter):
> python main.example.py

### Result
If all goes well, a random picture from the NASA archive will be posted onto your Twitter bot account. The date and title of the photo will be the photo's metadata and printed into the output.

### Troubleshooting
If you get an error, double-check the following:
- Twitter account (if you haven't used the "Automated" label, it's probably banned)
- secret.py (make sure your credentials are good)
- Dependencies (make sure they're installed correctly)
- Python version (try the latest one to be safe)

If none of these work, please submit a Github issue so I can help you out.
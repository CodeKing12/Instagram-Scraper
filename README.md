# Instagram Scraper

This script scrapes the Instagram profile of a given user and downloads the most liked video made within a specified number of days. The script will create two directories, `videos` and `descriptions`, where it will store the downloaded videos and the descriptions of the videos respectively. It also makes use of a `database.json` file to keep track of which videos have been previously scraped and a `settings.json` to retrieve configurations for the script.  The demo-settings file is an example of how a minimal settings file should look.

## Installation

This script requires Python 3.x and some packages that can be installed using pip. Start by creating a virtual environment, activating it and then installing the necessary packages using the following command:

```
pip install -r requirements.txt
```

## Usage

Start by logging into the instagram account you want to use to scrape on your default browser, then put in your username and password for the account in the settings.json file. You can have multiple settings for each profile, and the page will ask you for the setting you want to use each time it is run.

To use the script, simply run the `run.py` file. The script will log in to the Instagram account specified in the `settings.json` file and scrape the most liked video (from a randomly selected profile) made in the last n days (where n is the number of days specified in `settings.json`).

After the script has run, the most liked video will be downloaded into the `videos` folder and the description will be saved into the `descriptions` folder with the same file name as the video. The script will also update the `database.json` file to keep track of which videos have been previously scraped so as to scrape a different one on the next execution of the program.

## Customization

To customize the script, you can modify the `settings.json` file to change the following parameters:

- `username`: The username of the Instagram account you want to log in to.
- `password`: The password of the Instagram account you want to log in to.
- `days`: The number of days within which you want to scrape the most liked video.
- `profiles`: A list of Instagram profiles that you want to scrape videos from. You can specify multiple profiles and the script will randomly select one of them each time it is run.

Note that you should not modify the `database.json` file directly as the script uses it to keep track of which videos have been previously scraped.

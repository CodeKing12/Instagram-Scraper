import random, os
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
import wget, re, json
from instaloader import Instaloader, Profile, Post
from import_login.firefox_cookies import login_to_session

# Make the directories for saving the descriptions and the content of each video
if not os.path.isdir("videos"):
    os.mkdir("videos")
if not os.path.isdir("descriptions"):
    os.mkdir("descriptions")
if not os.path.isfile("database.json"):
    open("database.json", "x")
if not os.path.isfile("settings.json"):
    open("settings.json", "x").write('{}')


# Load the program settings and database from the settings.json and database.json files respectively
all_settings = json.loads(open("settings.json").read())

page_exists = False
# while not page_exists:
#     page = input("What page will you use today? ")
page = "page1"
if page in all_settings['pages'].keys():
    page_exists = True
    settings = all_settings['pages'][page]
    username = all_settings["username"]
    password = all_settings["password"]
    print("\nPage found.\n")
else:
    print("\n-----------------------------------------")
    print("Page not found in your settings file")
    print("-----------------------------------------\n")

database = json.loads(open("database.json").read())

# Select a random profile from the list of profiles in the program settings
input_profiles = settings["profiles"]
PROFILE = random.choice(input_profiles)
# PROFILE = "prioritykitty" #bestkittenvibes #catversum

# Initiate the Instaloader class and login to the instagram account specified in the settings
L = Instaloader()
login_to_session()

most_liked = Post.from_shortcode(context=L.context, shortcode="CqkTgelo28-")

# Download the video and description is there is a video made in the time range specified in FROM and TO
if most_liked != None:
    # Remove and store all hashtags from the original caption
    if most_liked.caption != None:
        edited_caption = most_liked.caption
        hashtag_list = ["#" + hashtag for hashtag in most_liked.caption_hashtags]
        for hashtag in sorted(hashtag_list, key=lambda tag: len(tag), reverse=True):
            edited_caption = edited_caption.replace(hashtag, "")
        # Convert the edited caption to a string, then remove all unnecessary spaces and newlines from the caption
        edited_caption = str(edited_caption)
        edited_caption = re.sub("\n+", "\n", edited_caption)
        edited_caption = re.sub(" +", " ", edited_caption)
        edited_caption = edited_caption.strip()
        # Append the specified string to the edited caption
        new_description = edited_caption + f"""
.
.
.
Credits: @{most_liked.profile}
.
{settings["hashtags"]} {" ".join(hashtag_list)}"""
    else:
        new_description = f"""Credits: @{most_liked.profile}\n.\n#cat #catsofinstagram #cats #catlover #instacat #catfood #catloaf #catchoftheday #cateringmurah #catsinstagram #catalina #cats_of_the_world #catlife🐾 #catto #catillustration #catperson #catfriends #hkcat #catselfies #caty #catholicblogger #cutecat #sleepingcat #catair"""
    print(new_description)
    print("-----------------------------------------")
    # Create a file name by combining the profile name and the date of the most liked vide
    file_name = most_liked.profile + "_" + str(most_liked.date_utc).replace(" ", "-")
    
    print("Downloading Video...")
    # Download the most liked video
    print(most_liked.video_url)
    print(most_liked.mediacount)
    if most_liked.mediacount > 1:
        file_index = 1
        for node in most_liked.get_sidecar_nodes():
            wget.download(node.display_url, f"videos/{file_name}_{file_index}.mp4")
            file_index += 1
    else:
        video = wget.download(most_liked.video_url, f"videos/{file_name}.mp4")
    print("")

    # Open the descriptions file with the specified file name, insert the caption there and close the file
    try:
        desc = open(f"descriptions/{file_name}.txt", "x")
    except FileExistsError:
        desc = open(f"descriptions/{file_name}.txt", "w")

    desc.write(new_description)
    desc.close()

    # Add the scraped post to the database
    database[PROFILE].append(most_liked.mediaid)
    open("database.json", "w").write(json.dumps(database))
# Inform the user if there are no videos found in the specified time range
else:
    print(f"No videos found in @{PROFILE} from the last 28 days")
    print("-----------------------------------------")

    # "profiles": ["kittynoodlez", "catieepieee", "cutecatsvibeez", "kittenscuddlez", "prioritykitty", "dailydoseeofcats", "bestkittenvibes", "catversum"],
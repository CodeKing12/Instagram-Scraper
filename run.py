import random, requests
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
import wget

from instaloader import Instaloader, Profile

input_profiles = ["bestkittenvibes", "kittynoodlez", "catieepieee", "cutecatsvibeez", "kittenscuddlez", "catversum", "prioritykitty", "dailydoseeofcats"]

PROFILE = random.choice(input_profiles)
# PROFILE = "bestkittenvibes"

L = Instaloader()

TO = datetime.now()
FROM = TO - timedelta(days=28)

profile = Profile.from_username(L.context, PROFILE) 
all_posts = profile.get_posts()
posts_in_date = [post for post in takewhile(lambda p: p.date > FROM, dropwhile(lambda p: p.date > TO, all_posts))]
engagements = [post.comments + post.likes for post in posts_in_date]

highest_engage = 0
most_liked = None
for index, post in enumerate(posts_in_date):
    total_engagement = post.comments + post.likes
    if total_engagement > highest_engage:
        highest_engage = total_engagement
        most_liked = post



# print(PROFILE)
# print(posts_in_date)
# print(highest_engage)
# print(most_liked)
print("-----------------")
if most_liked != None:
    new_description = most_liked.caption.strip() + "\n" + f"""
.
.
.
Credits: @{most_liked.profile}
.
#cat #catsofinstagram #cats #catlover #instacat #catfood #catloaf #catchoftheday #cateringmurah #catsinstagram #catalina #cats_of_the_world #catlife🐾 #catto #catillustration #catperson #catfriends #hkcat #catselfies #caty #catholicblogger #cutecat #sleepingcat #catair"""
    new_description 
    print(new_description)
    print("-----------------------------------------")
    file_name = most_liked.profile + "_" + str(most_liked.date_utc).replace(" ", "-")
    
    print("Downloading Video...")
    # video = requests.get(most_liked.video_url)
    # open(f"videos/{file_name}.mp4", "wb").write(video.content)
    video = wget.download(most_liked.video_url, f"videos/{file_name}.mp4")
    print("")

    try:
        desc = open(f"descriptions/{file_name}.txt", "x")
    except FileExistsError:
        desc = open(f"descriptions/{file_name}.txt", "w")

    desc.write(new_description)
    desc.close()
else:
    print("No videos found")
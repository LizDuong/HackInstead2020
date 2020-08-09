import praw
from urllib.request import urlopen
from shutil import copyfileobj
import twitterBot
import time
import schedule
import time

reddit = praw.Reddit(client_id='dj2PemOp_g1u2Q',
                     client_secret='MqHiGzYVQjWaOXT_zeNl9vmMc9U',
                     user_agent='PSBattle')
temp_id = 0


def grab_a_pic():
    global temp_id
    hot_posts = reddit.subreddit('MechanicalKeyboards').top("day", limit=4)
    for post in hot_posts:
        if temp_id == post.id:
            continue
        url = str(post.url)
        with urlopen(url) as in_stream, open('top.jpg', 'wb') as out_file:
            copyfileobj(in_stream, out_file)
        temp_id = post.id
        time.sleep(3)
        twitterBot.main(post.title, post.author)
        break


if __name__ == "__main__":
    grab_a_pic()

schedule.every(6).hours.do(grab_a_pic)
while 1:
    schedule.run_pending()
    time.sleep(1)



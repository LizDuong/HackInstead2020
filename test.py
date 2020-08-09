import praw
import re
from imgur_downloader import ImgurDownloader

reddit = praw.Reddit(client_id='dj2PemOp_g1u2Q',
                     client_secret='MqHiGzYVQjWaOXT_zeNl9vmMc9U',
                     user_agent='PSBattle')

hot_posts = reddit.subreddit('MechanicalKeyboards').top()

for post in hot_posts:
    if not post.stickied:
        if len(post.comments) < 5:
            continue
        print(f'Title: {post.title}, ups: {post.ups}')
        #post.comment_sort = "top"
        #REGEX_TEST = r"(https?:\/\/(i\.)?imgur\.com\/.+(.jpg|png)?)"
        #p = re.compile(REGEX_TEST, re.IGNORECASE)
        """for x in range(2):
            if 'imgur' in post.comments[x].body:
                matches = p.findall(post.comments[x].body)
            else:
                matches = p.findall(post.comments[x+1].body)
            matches = matches[0][0]
            if ')' in matches:
                matches = matches[:-1]
            print(matches)
            ImgurDownloader(matches, '.').save_images()"""


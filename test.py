import praw

reddit = praw.Reddit(client_id='dj2PemOp_g1u2Q',
                     client_secret='MqHiGzYVQjWaOXT_zeNl9vmMc9U',
                     user_agent='PSBattle')


hot_posts = reddit.subreddit('photoshopbattles').hot(limit=7)

for post in hot_posts:
    if not post.stickied:
        ##print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(post.title))
        print(f'Title: {post.title}, ups: {post.ups}')
        post.comment_sort = "top"
        for x in range(2):
            if 'imgur' in post.comments[x].body:
                print(post.comments[x].body)
        #for comment in post.comments:
            #print(comment.body)

import tweepy
import time

import tweepy


def main():
    twitter_auth_keys = {
        "consumer_key": "REPLACE_THIS_WITH_YOUR_CONSUMER_KEY",
        "consumer_secret": "REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET",
        "access_token": "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN",
        "access_token_secret": "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    api = tweepy.API(auth)

    tweet = "Another day, another #scifi #book and a cup of #coffee"
    status = api.update_status(status=tweet)


if __name__ == "__main__":
    main()



print('print')
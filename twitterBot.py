import tweepy


def main():
    twitter_auth_keys = {
        "consumer_key": "hL6RL0YB9XIC37khVLqw8E3kj",
        "consumer_secret": "PuPJDr3kCfleaZ6IoeNyNru1GnF4HlC5CGJpU49d9yZBVb81zX",
        "access_token": "1292255341913178113-m3nKjzcr2OwdrdXOfGiV71KzKtCwYr",
        "access_token_secret": "BVyD2st2lkkp03dXyjkhgKgqvegAQqMhEx0b37ZwkbGoW"
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

    tweet = "Allekusu"
    status = api.update_status(status=tweet)


if __name__ == "__main__":
    main()


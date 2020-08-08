import tweepy
import time

CONSUMER_KEY = 'API key'
CONSUMER_SECRET = 'API secret key'
ACCESS_KEY = 'access token'
ACCESS_SECRET = 'access token secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


print(“what the faaaack”)
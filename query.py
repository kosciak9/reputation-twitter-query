import datetime
from db import Tweet, TweetDelta
from twitterscraper import query_tweets


def get_tweet(tweet_id):
    """Get tweet from core app
    """
    return False


def add_tweet(tweet):
    """Send tweet over to core app
    """
    print(tweet)
    pass


def scrap():
    """Probe tweets and store any stats (likes, retweets, ...) changes
    """
    bgdate = (datetime.date.today() - datetime.timedelta(days=3))
    twts = query_tweets('Polityka', begindate=bgdate, enddate=datetime.date.today())
    for twt in twts:
        tweet = Tweet.get_or_create(id=twt.tweet_id)
        dt = TweetDelta.create(tweet=tweet, likes=twt.likes)

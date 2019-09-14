from db import db, Tweet, TweetDelta
from query import scrap

"""Probe tweets 5 times in a row
"""

db.connect()
db.create_tables([Tweet, TweetDelta])

for i in range(1, 5):
    scrap()

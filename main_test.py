from db import db, Tweet, TweetDelta
from query import scrap, pick

"""Probe tweets 6 times in a row
"""

db.connect()
db.create_tables([Tweet, TweetDelta])

for i in range(1, 6):
    scrap()
print(pick(threshold=1))

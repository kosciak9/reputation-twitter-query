from flask import Flask
from threading import Thread
from scraper import run, Tweet, TweetDelta, db

app = Flask(__name__)

@app.route('/promote/<string:tweet_id>')
def promote(tweet_id):
    tweet = Tweet.get_or_create(id=tweet_id)
    tweet[0].promote()
    return tweet[0].serialize()

def routine():
    """Run scraper
    """
    run(5)

if __name__ == "__main__":
    db.connect()
    db.create_tables([Tweet, TweetDelta])
    t = Thread(target=routine)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=1337)

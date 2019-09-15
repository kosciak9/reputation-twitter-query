from flask import Flask
from threading import Thread
from scraper import run

app = Flask(__name__)

@app.route('/promote/<string:tweet_id>')
def promote(tweet_id):
    pass

def routine():
    """Run scraper
    """
    run(5)

if __name__ == "__main__":
    t = Thread(target=routine)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=1337)

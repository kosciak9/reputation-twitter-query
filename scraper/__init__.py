import time
from .db import *
from .query import *

def run(interval=5):
    secs = interval*60
    while True:
        scrap()
        picked = pick(threshold=10)
        time.sleep(secs)

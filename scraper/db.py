import datetime, numpy as np
from peewee import (SqliteDatabase, Model,
                    CharField, IntegerField,
                    DateTimeField, ForeignKeyField,
                    TextField)


db = SqliteDatabase('scraps.db')


class Tweet(Model):
    class Meta:
        database = db

    id = CharField(primary_key=True)
    category = CharField(default='Polityka')
    tweet_url = CharField(default='')
    html_content = TextField(default='')
    date_posted = DateTimeField(default=datetime.datetime.now())

    @property
    def avg_gross(self):
        if self.deltas.count() < 2:
            return 0
        likes = np.array([np.float(delta.likes) for delta in self.deltas])
        likedeltas = np.diff(likes)
        times = np.array([delta.timestamp for delta in self.deltas])
        timedeltas = np.array(np.diff(times))
        secs = np.array([np.float(td.seconds)/np.float(60*5) or np.float(1) for td in timedeltas])
        return float(np.mean(np.divide(likedeltas, secs)))

    def serialize(self):
        d = {
                'tw_id': self.id,
                'category': self.category,
                'tweet_url': self.tweet_url,
                'html_content': self.html_content,
                'date_posted': self.date_posted.isoformat(),
                'likes_delta': round(self.avg_gross)
                }
        return d

    def promote(self):
        time = datetime.datetime.now()
        timedelta = datetime.timedelta(minutes=5)
        likes = 300
        for i in range(1, 6):
            TweetDelta.create(tweet=self, likes=likes)
            time += timedelta
            likes += 200


class TweetDelta(Model):
    class Meta:
        database = db

    tweet = ForeignKeyField(Tweet, backref='deltas')
    likes = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now())

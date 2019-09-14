import datetime, numpy as np
from peewee import (SqliteDatabase, Model,
                    CharField, IntegerField,
                    DateTimeField, ForeignKeyField)


db = SqliteDatabase('scraps.db')


class Tweet(Model):
    class Meta:
        database = db

    id = CharField(primary_key=True)

    @property
    def avg_gross(self):
        likes = [delta.likes for delta in self.deltas]
        return np.mean(np.diff(likes))


class TweetDelta(Model):
    class Meta:
        database = db

    tweet = ForeignKeyField(Tweet, backref='deltas')
    likes = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now())

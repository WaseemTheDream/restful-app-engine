"""
Books model.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


from google.appengine.ext import db


class Book(db.Model):
    title = db.StringProperty(required=True,
                              default='Unknown title')
    author = db.StringProperty(required=True,
                               default='Uknown author')
    release_date = db.StringProperty(required=True,
                                     default='Unknown release date')
    keywords = db.StringProperty()
    json_attributes = ['title', 'author', 'release_date', 'keywords']

    def load_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

    def to_json(self):
        json = {}
        for attr in self.json_attributes:
            json[attr] = getattr(self, attr)
        return json



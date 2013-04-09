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
        def load(key, value):
            if key in self.json_attributes:
                setattr(self, key, value)
        print json.items()
        map(lambda arg: load(*arg), json.items())

    def to_json(self):
        json = {}
        map(lambda attr: json.update({attr: getattr(self, attr)}),
            self.json_attributes)
        json['key'] = str(self.key())
        return json


def get_books():
    return map(lambda book: book.to_json(), Book.all())

def get_book(key):
    return Book.get(key).to_json()

def post_book(book_json):
    book = Book()
    book.load_json(book_json)
    book.put()
    return str(book.key())
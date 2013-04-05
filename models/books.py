"""
Books model.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


from google.appengine.ext import db


class Book(db.Model):
    title = db.StringProperty(required=True)
    author = db.StringProperty(required=True)
    release_date = db.DateTimeProperty(required=True,
                                       auto_add_now=True)
    keywords = db.StringProperty()
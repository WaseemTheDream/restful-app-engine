"""
API for books.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import json
import webapp2

from models import Books

class BooksHandler(webapp2.RequestHandler):
    def get(self):
        books = Books.get_books()
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(books))


app = webapp2.WSGIApplication([
    ('/api/books', BooksHandler)
], debug=True)
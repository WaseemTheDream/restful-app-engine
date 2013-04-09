"""
API for books.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import json
import logging
import webapp2

from models import Books

class BooksHandler(webapp2.RequestHandler):
    def get(self):
        books = Books.get_books()
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(books))

class BookHandler(webapp2.RequestHandler):
    def get(self):
        # TODO: Better way of acquiring this?
        book_key = self.request.uri.rsplit('/', 1)[-1]

        logging.info('GET Request for Book with key:' + book_key)
        book = Books.get_book(book_key)
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(book))


app = webapp2.WSGIApplication([
    ('/api/books', BooksHandler),
    ('/api/books/.*', BookHandler)
], debug=True)
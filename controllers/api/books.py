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
        def get_books():
            books = Books.get_books()
            self.json_out(books)

        def get_book():
            book_key = self.get_key()
            book = Books.get_book(book_key)
            self.json_out(book)

        if self.request.uri.endswith('books'):
            get_books()
        else:
            get_book()

    def post(self):
        book_json = json.loads(self.request.body)
        book_key = Books.post_book(book_json)
        self.json_out(book_key)

    def put(self):
        book_json = json.loads(self.request.body)
        book_key = self.get_key()
        book_key = Books.put_book(book_key, book_json)
        self.json_out(book_key)

    def delete(self):
        book_key = self.get_key()
        Books.delete_book(book_key)


    def get_key(self):
        # TODO: Better way of acquiring this?
        return self.request.uri.rsplit('/', 1)[-1]

    def json_out(self, json_data):
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(json_data))
        

app = webapp2.WSGIApplication([
    ('/api/books.*', BooksHandler)
], debug=True)
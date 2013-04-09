"""
API for books.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import json
import webapp2


class BooksHandler(webapp2.RequestHandler):
    def get(self):
        books = [
            {
                'title': "JS the good parts",
                'author': "John Doe",
                'releaseDate': "2012",
                'keywords': "JavaScript"
            }, {
                'title': "CS the better parts",
                'author': "John Doe",
                'releaseDate': "2012",
                'keywords': "CoffeeScript"
            }, {
                'title': "Scala for the impatient",
                'author': "John Doe",
                'releaseDate': "2012",
                'keywords': "Scala"
            }, {
                'title': "American Psyco",
                'author': "Bret Easton Ellis",
                'releaseDate': "2012",
                'keywords': "Novel"
            }, {
                'title': "Eloquent JavaScript",
                'author': "John Doe",
                'releaseDate': "2012",
                'keywords': "JavaScript"
            }
        ]
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(books))


app = webapp2.WSGIApplication([
    ('/api/books', BooksHandler)
], debug=True)
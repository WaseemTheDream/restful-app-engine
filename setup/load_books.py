"""
Run this file from the App Engine interactive remote API.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import os
import json

from models import Books

LOCAL_DIR = os.path.dirname(__file__)

def main():
    print 'Opening books.json'
    path = os.path.join(os.path.split(__file__)[0], 'books.json')
    json_data = open(path, 'r').read()
    books = json.loads(json_data)['books']

    print 'Loading books into database...'
    for book_json in books:
        book = Books.Book()
        book.load_json(book_json)
        book.put()
        print 'Loaded', book.title

    print 'Done loading.'

if __name__ == '__main__':
    main()
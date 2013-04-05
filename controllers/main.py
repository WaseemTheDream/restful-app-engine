"""
Digital library app.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

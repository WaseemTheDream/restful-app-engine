"""
Digital library app.
"""

__author__ = 'Waseem Ahmad <waseem@rice.edu>'


import os
import jinja2
import webapp2


MAIN_DIR = os.path.dirname(__file__)
PAGES_DIR = os.path.join(MAIN_DIR, '../views')

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(PAGES_DIR))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('index.html')
        self.response.out.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

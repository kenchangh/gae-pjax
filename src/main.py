##########

import webapp2
from webapp2 import Route

from handlers.handlers import FrontPage, Dashboard, HomePage, CommentHandler, JsonHandler

##########

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

##########

app = webapp2.WSGIApplication([
      ('/', FrontPage),
      ('/home', HomePage),
      ('/comments', CommentHandler),
      ('/dashboard', Dashboard),
      Route('/json/<company>', handler = JsonHandler, name = 'json-item'),
      Route('/dashboard/<item>', handler = Dashboard, name = 'dashboard-item')],
      config = config, debug = True)

if __name__ == '__main__':
    app.run()
    

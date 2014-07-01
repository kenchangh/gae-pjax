##########

import logging
import webapp2
from webapp2 import Route

from base_handler import BaseHandler

##########

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

##########

class BasePage(BaseHandler):
    
    def get(self):
        self.render('base.html')
        
    def post(self):
        pass
        
        
class Transportation(BaseHandler):

    def get(self, **kw):
        
        transport = kw['transportation']
        
        self.pjax(transport + ".html")
        
    def post(self):
        pass

##########

app = webapp2.WSGIApplication([
      ('/', BasePage),
      Route('/transport/<transportation>', handler = Transportation),],
      config = config, debug = True)

if __name__ == '__main__':
    app.run()
    

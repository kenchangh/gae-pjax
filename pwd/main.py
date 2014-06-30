#!/usr/bin/env python
##########

import web
from handlers.home import HomePage
from handlers.login import LoginPage
from handlers.front import FrontPage
from handlers.chat import ChatHandler
from handlers.work import WorkPage

##########

urls = ('/', 'FrontPage',
        '/home', 'HomePage',
        '/work', 'WorkPage',
        '/login', 'LoginPage',
        '/chat', 'ChatHandler')

app = web.application(urls, globals())

##########

if __name__ == "__main__":
    app.run()


import urllib

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import tornado

from urllib.parse import urlparse



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class EmailHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_body_argument("Full Name")
        self.write(username)




def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
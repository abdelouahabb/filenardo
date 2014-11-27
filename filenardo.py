# -*- coding: utf-8 -*-

import os
import glob
import argparse
import tornado.web
import tornado.httpserver
from tornado.options import define, options

pat = os.path.dirname(__file__)

define("path", default=pat, help="The Folder")
define("url", default='127.0.0.1', help="The URL")
define("port", default=8888, type=int, help="Use a free port")

options.parse_command_line()

path = options.path

names = os.walk(path).next()[2]

files = []

if path.endswith("/"):
    path = path[:-1]

for fil in glob.glob(path+'/*.*'):
    files.append(fil)


class FilesLister(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write('<ol>')
        for i in zip(files, names):
            self.write('<li><a href="{0}" title="{1}">{0}</a></li>'.format(i[1], i[0]))
        self.write('<ol/>')
        self.finish()

settings = dict({
    "compress_response": True,
})


urls = [
    (r"/", FilesLister),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": r"{0}".format(path)}),
]

application = tornado.web.Application(urls, **settings)

if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port=options.port, address=options.url)
    print 'Running on {0}:{1}'.format(options.url, options.port)
    tornado.ioloop.IOLoop.instance().start()

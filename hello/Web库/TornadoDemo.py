# Tornado一个异步web框架 通过使用非阻塞I/O流

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write('Hello World hanxiaocu')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

# http://127.0.0.1:8888/
if __name__ == '__main__':
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()

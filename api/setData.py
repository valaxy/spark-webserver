# encoding=utf-8

from tornado.websocket import *


class SetDataHandler(WebSocketHandler):
    def open(self):
        print("some one connect")

    def on_message(self, message):
        self.write_message({
            "time": 19993,
            "data": 10.8
        })




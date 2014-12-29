# encoding=utf-8
# 获取自定服务器时间的数据

from tornado.websocket import *


class GetDataHandler(WebSocketHandler):
    def open(self):
        print("some one connect")

    def on_message(self, message):
        self.write_message({
            "time": 19993,
            "data": 10.8
        })

    def check_origin(self, origin):
        return True






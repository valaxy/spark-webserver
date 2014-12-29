# encoding = utf-8

from tornado.web import *
from datetime import datetime
import math
import random


class FirstGetDataHandler(RequestHandler):
    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write({
            "state": True,
            "time": math.floor(datetime.today().timestamp() * 1000),
            "data": random.random() * 100
        })






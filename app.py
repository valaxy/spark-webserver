from tornado.web import *
from tornado.ioloop import *

from api.getData import *
from api.setData import *

app = Application([
    ("/api/getData", GetDataHandler),
    ("/api/setData", SetDataHandler),
    ("/content/(.*)", StaticFileHandler, {"path": "content"}),
])

app.listen(9876)
IOLoop.current().start()
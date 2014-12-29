from tornado.web import *
from tornado.ioloop import *

from api.getData import *
from api.setData import *
from api.firstGetData import *

app = Application([
    ("/api/getData", GetDataHandler),
    ("/api/setData", SetDataHandler),
    ("/api/first-get-data", FirstGetDataHandler),
    ("/content/(.*)", StaticFileHandler, {"path": "content"}),
], debug=True)

app.listen(9876)
IOLoop.current().start()
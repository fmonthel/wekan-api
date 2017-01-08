# flake8: noqa: E402, F401

import core.app

app = core.app.app
db = core.app.init_db()

from api import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)

### Needed to enable websocket ###
from testapp import app, socketio

import eventlet
eventlet.monkey_patch()
#################################


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0')

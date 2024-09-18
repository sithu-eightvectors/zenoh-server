from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] =  'web_socket_secret_key'

from zenoh_server.api.routes import subscribe_bp
app.register_blueprint(subscribe_bp)

socketio = SocketIO(app, cors_allowed_origins="*")

# Import and set up the WebSocket events handler
from zenoh_server.api.socketio_events import SocketIOHandler
handler = SocketIOHandler(socketio)
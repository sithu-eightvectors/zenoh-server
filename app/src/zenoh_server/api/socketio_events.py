from flask_socketio import SocketIO, emit

class SocketIOHandler:
    def __init__(self, socketio: SocketIO):
        self.socketio = socketio
        self.setup_events()

    def setup_events(self):
        self.socketio.on_event('connect', self.handle_connect)
        self.socketio.on_event('message', self.handle_message)
        self.socketio.on_event('disconnect', self.handle_disconnect)

    def handle_connect(self):
        emit('response', {'message': 'Connected!'})

    def handle_message(self, data):
        print(f"Received message: {data}")
        emit('response', {'message': 'Message received!'})

    def handle_disconnect(self):
        print("Client disconnected")


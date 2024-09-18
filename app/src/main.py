import asyncio
import threading
from zenoh_server import app, socketio

def run_flask_app():
    app.run(debug=True, port=8080)

def run_websocket_server():
    asyncio.run(socketio.run(app, host='0.0.0.0', port=443))

if __name__ == "__main__":
    run_flask_app()
    flask_thread = threading.Thread(target=run_websocket_server)
    flask_thread.run()
    
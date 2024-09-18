from zenoh_server import app, socketio
import asyncio

def run_websocket_server():
    asyncio.run(socketio.run(app, host='0.0.0.0', port=443))

if __name__ == "__main__":
    run_websocket_server()
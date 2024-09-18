import zenoh

class ZenohClient:
    def __init__(self):
        self.zenoh_session = None
        self.endpoint = None
        self.subscriptions = {}

    async def connect(self, endpoint):
        if self.zenoh_session:
            print("Already connected to a Zenoh bridge.")
            return

        self.endpoint = endpoint
        try:
            self.zenoh_session = await zenoh.open({"peer": self.endpoint})
            print(f"Connected to Zenoh bridge at {self.endpoint}")
        except Exception as e:
            print(f"Failed to connect to Zenoh bridge: {e}")

    async def disconnect(self):
        if not self.zenoh_session:
            print("No active Zenoh bridge connection to disconnect from.")
            return

        try:
            await self.zenoh_session.close()
            self.zenoh_session = None
            self.endpoint = None
            self.subscriptions.clear()
            print("Disconnected from Zenoh bridge.")
        except Exception as e:
            print(f"Failed to disconnect from Zenoh bridge: {e}")

    async def subscribe(self, topic_name):
        if not self.zenoh_session:
            print("Not connected to a Zenoh bridge.")
            return

        if topic_name in self.subscriptions:
            print(f"Already subscribed to topic: {topic_name}")
            return

        try:
            def callback(data):
                print(f"Received data from topic {topic_name}: {data}")

            sub = await self.zenoh_session.subscribe(topic_name, callback)
            self.subscriptions[topic_name] = sub
            print(f"Subscribed to topic: {topic_name}")
        except Exception as e:
            print(f"Failed to subscribe to topic {topic_name}: {e}")

    async def is_connected(self):
        return self.zenoh_session is not None


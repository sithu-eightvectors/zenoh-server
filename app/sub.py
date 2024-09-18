import zenoh

def process_scan_data(data):
    print(f"-----{data}")

def main():
    # Initialize Zenoh session
    session = zenoh.open(zenoh.Config.from_json5({"connect" : { "endpoints" : ["global-nlb-4e6357043b4d27e6.elb.ap-southeast-1.amazonaws.com"] }}))

    # Define the resource path to subscribe to
    resource_path = 'chatter'

    # Create a subscriber for the given resource path
    sub = session.declare_subscriber(resource_path, lambda sample: process_scan_data(sample.payload.decode("utf-8")))

    try:
        print(f"Subscribed to {resource_path}. Waiting for data...")
        # Keep the subscriber running
        while True:
            pass
    except KeyboardInterrupt:
        print("Subscriber interrupted by user")
    finally:
        # Clean up
        session.close()

if __name__ == "__main__":
    main()
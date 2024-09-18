import zenoh
import time
import json
import numpy as np

def create_fake_scan():
    # Create a fake LaserScan message
    scan = {
        "header": {
            "stamp": {
                "sec": int(time.time()),  # Current time in seconds
                "nanosec": int((time.time() % 1) * 1e9)  # Current time in nanoseconds
            },
            "frame_id": "laser_frame"
        },
        "angle_min": -1.57,  # -90 degrees
        "angle_max": 1.57,   # 90 degrees
        "angle_increment": 0.01,
        "time_increment": 0.0,
        "scan_time": 0.1,
        "range_min": 0.1,
        "range_max": 10.0,
        "ranges": list(np.random.uniform(0.1, 10.0, 314)),  # Random ranges
        "intensities": list(np.random.uniform(0.0, 1.0, 314))  # Random intensities
    }
    return scan

def main():
    zenoh.init_logger()
    # Initialize Zenoh session
    session = zenoh.open()

    # Define the resource path
    resource_path = 'chatter'

    try:
        while True:
            # Create fake LaserScan data
            scan_data = create_fake_scan()
            
            # Convert data to JSON string
            scan_json = json.dumps(scan_data)
            
            # Publish data
            session.put(resource_path, scan_json)
            print(f"Published data to {resource_path}")

            # Wait for 3 seconds
            time.sleep(3)
    except KeyboardInterrupt:
        print("Publisher interrupted by user")
    finally:
        # Clean up
        session.close()

if __name__ == "__main__":
    main()

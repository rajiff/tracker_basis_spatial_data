from vehicle_location_fetch import get_vehicle_location
from route import route_stops
from find_distance import is_within_distance
from datetime import datetime
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    filename='bus_tracker.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

def track_bus_near_locations():
    # Fetch latest or current location 
    # compare if it is within a certain distance from the bus stop locations
    # If yes, then print the message using the template of the stop and log the timestamp when it was near

    # Fetch latest vehicle location
    location_now = get_vehicle_location()

    # print(location_now)

    if location_now.get('result') == 'success':
        # Check if it is near any route stops
        for stop in route_stops:
            # Calculate the distance between the current location and the stop
            distance = is_within_distance(
                [float(location_now['latitude']), float(location_now['longitude'])],
                [stop.get('latitude'), stop.get('longitude')],
                stop['nearDistanceMts'],
                'm'
            )

            if distance == True:
                print(f"{datetime.now().strftime("%d-%m-%Y %H:%M:%S")} ==> {stop['alertMsgTemplate']}")
            else:
                pass
    else:
        print("Failed to fetch vehicle location")
        
    
    return

while True:
    track_bus_near_locations()
    time.sleep(10)

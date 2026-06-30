import requests
import time
from datetime import datetime

def track_vehicle_raw():

    # 1. Send the HTTP GET request
    url = "https://cordontrack.com/api/v1/vehicle/live_vehicles_urltrack?rto=KA05AF8760"
    response = requests.get(url)

    # 2. Check if the request was successful (Status Code 200)
    if response.status_code >= 200 and response.status_code < 300:
        # 3. Parse the JSON response body
        data = response.json()

        # print(f"Type of data {type(data)}")
        
        # 4. Access the parsed dictionary data
        # print(f"Time: {data['data'][0]['datetime']}")
        # print(f"status: {data['status']}")
        # # print(f"message: {data['message']}")
        # print(f"rto: {data['data'][0]['rto']}")
        # print(f"latitude: {data['data'][0]['latitude']}")
        # print(f"longitude: {data['data'][0]['longitude']}")
        # print(f"GPS: {data['data'][0]['gps_status']}")

        # Print the data in one line
        print(f"As of {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} Vehicle status at {data['data'][0]['datetime']} ({data['status']} | {data['data'][0]['gps_status']}) Loc: {data['data'][0]['latitude']} {data['data'][0]['longitude']} speed {data['data'][0]['speed']} {data['data'][0]['ignition_status']} {data['data'][0]['location']})")

        # idle_since
    else:   
        print(f"Failed to fetch data. Status: {response.status_code}")

# Invoke tracking every 20 seconds
    
while True:
    track_vehicle_raw()
    time.sleep(10)

# KRB Stop
#12.85892410647419, 77.57061252284825

# Start alerting when reaches
# 12.860675671891553, 77.55924935755357
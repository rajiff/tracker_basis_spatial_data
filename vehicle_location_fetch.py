import requests
import time
from datetime import datetime


def get_vehicle_location():

    # 1. Send the HTTP GET request
    url = "https://cordontrack.com/api/v1/vehicle/live_vehicles_urltrack?rto=KA05AF8760"
    response = requests.get(url)
    vehicle_tracker_data = data = {
            "result": "error",
            "error": "unknown"
    }

    # 2. Check if the request was successful (Status Code 200)
    if response.status_code >= 200 and response.status_code < 300:
        # 3. Parse the JSON response body with useful fields
        data = response.json()

        # print(f"As of {datetime.now().strftime("%d-%m-%Y %H:%M:%S")} 
        # Vehicle status at {data['data'][0]['datetime']} ({data['status']} | 
        # {data['data'][0]['gps_status']}) Loc: {data['data'][0]['latitude']} {data['data'][0]['longitude']} speed {data['data'][0]['speed']} {data['data'][0]['ignition_status']}")

        vehicle_tracker_data = {
            "result": "success",
            "status": data.get("status"),
            "message": data.get("message"),
            "gps_status": data.get("data")[0].get("gps_status"),
            "latitude": data.get("data")[0].get("latitude"),
            "longitude": data.get("data")[0].get("longitude"),
            "speed": data.get("data")[0].get("speed"),
            "trackedAt": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "statusAt": data.get("data")[0].get("datetime"),
            "ignition": data.get("data")[0].get("ignition_status")
        }

    else:
        # return error status
        vehicle_tracker_data = {
            "result": "error",
            "error": response.text
        }
    
    return vehicle_tracker_data

# Vehicle tracking data response example
# {
#     "status": true,
#     "message": "List Vehicle success",
#     "data": [
#         {
#             "id": "67715",
#             "rto": "KA05AF8760",
#             "imei": "866777073101111",
#             "sim": "5754304143919",
#             "v_type": "car",
#             "vehicle_category": null,
#             "d_name": null,
#             "distance": null,
#             "location": "0.9 Kms From 2003  Bengaluru  Karnataka 560062  India",
#             "latitude": "12.843695",
#             "longitude": "77.541926666667",
#             "s_lat": null,
#             "n_lat": null,
#             "w_lon": null,
#             "e_lon": null,
#             "direction": "33",
#             "datetime": "29-06-2026 12:50:16",
#             "speed": "0",
#             "gps_status": "1",
#             "gsm_singnal_strength": "22",
#             "ac_status": null,
#             "ac_since": "0",
#             "satilites_in_view": "0",
#             "fuel_value": "0",
#             "idle_since": "0",
#             "geo_since": "0",
#             "ignition_status": "0",
#             "power_status": null,
#             "panic_status": "0",
#             "angle_polling_alert": null,
#             "harsh_breaking": null,
#             "harsh_acceleration": null,
#             "case_open_switch_status": null,
#             "door_status": null,
#             "internal_battery_voltage": "4",
#             "external_battery_voltage": null,
#             "acumulated_distance": "12295450",
#             "distance_today": "0",
#             "geo_status": null,
#             "geo_id": null,
#             "citygeo_status": null,
#             "citygeo_id": null,
#             "citygeo_since": "0",
#             "geo_name": null
#         }
#     ]
# }
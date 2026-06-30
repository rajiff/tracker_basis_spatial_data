import json
import urllib.request

def get_road_distance(lon1, lat1, lon2, lat2):
    # OSRM expects: longitude,latitude;longitude,latitude
    url = f"http://project-osrm.org{lon1},{lat1};{lon2},{lat2}?overview=false"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            
            # Distance is returned in meters
            distance_meters = data['routes'][0]['distance']
            duration_seconds = data['routes'][0]['duration']
            
            return {
                "meters": distance_meters,
                "kilometers": distance_meters / 1000,
                "duration_mins": duration_seconds / 60
            }
    except Exception as e:
        print(f"Error fetching route: {e}")
        return None

# --- Example: Route between two coordinates ---
result = get_road_distance(77.58370, 12.88170, 77.57057, 12.85901)

if result:
    print(f"Road Distance: {result['kilometers']:.2f} km")
    print(f"Travel Time: {result['duration_mins']:.1f} minutes")

import math

def is_within_distance(coord1, coord2, max_distance, unit='km'):
    """
    Checks if two coordinates are within a specified distance.
    coord1, coord2: Tuples of (latitude, longitude)
    max_distance: Numeric limit (e.g., 5.0)
    unit: 'km' for kilometers, 'm' for meters
    """
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    # Haversine formula math
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Earth's radius
    radius = 6371.0088 if unit == 'km' else 6371008.8
    
    actual_distance = c * radius
    return actual_distance <= max_distance
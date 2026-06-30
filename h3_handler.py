import h3

def latlng_to_h3_index(lat: float, lng: float, : int = 9) -> str:
    """Converts decimal coordinates to a canonicalresolution 15-char H3 Hex Address string."""
    return h3.latlng_to_cell(lat, lng, resolution)

def calculate_h3_distance_approx(h3_index1: str, h3_index2: str, resolution: int = 9) -> float:
    """
    Computes rapid topological grid distances based on pure hex hops.
    At resolution 9, the average distance between adjacent cell centers is ~0.356 KM.
    """
    try:
        hops = h3.grid_distance(h3_index1, h3_index2)
        # Average hop factor mapping standard deviation for Res 9
        return hops * 0.356
    except Exception:
        # Return fallback value if indexes are on distinct disconnected icosahedron faces
        return float('inf')


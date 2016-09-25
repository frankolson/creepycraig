#
# File to store functions related to filtering
#
from math import radians, cos, sin, asin, sqrt

# check if in desired neighborhoods
def in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

def in_hood(location, neighborhoods):
    for n in neighborhoods:
        if n in location.lower():
            return n
    return ""

def coord_distance(p1, p2):
    p1_lat, p1_lon, p2_lat, p2_lon = map(radians, [p1[0], p1[1], p2[0], p2[1]])

    # Haversine Formula in Python
    dlon = p2_lon - p1_lon
    dlat = p2_lat - p1_lat
    a = sin(dlat/2)**2 + cos(p1_lat) * cos(p2_lat) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    m = km * 0.621371
    return m

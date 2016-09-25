#
# File to store functions related to filtering
#

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

def near_bart():

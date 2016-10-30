#
# File to store or the variables that may to need be changed frequently
#
from secret import *

## APARTMENT PREFERENCES
MAX_PRICE = 2500
MIN_PRICE = 500

CEILINGS = {
    # two rooms
    "2" : 1950,
    # three rooms
    "3" : 2700
}

## Location
SITE = 'sfbay'
AREAS = ["eby", "nby", "sby", "sfc"]
BOXES = {
    # Berkeley
    "berkeley": [
        [37.846226, -122.234179],
        [37.905668, -122.327065]
    ],
    # Castro Valley
    "castro_valley": [
        [37.678831, -122.002371],
        [37.752628, -122.130875]
    ],
    # Mountain View
    "mountain_view": [
        [37.35676, -122.044672],
        [37.450879, -122.117862]
    ],
    # Oakland
    "adams_point": [
        [37.808027, -122.2493801],
        [37.817327, -122.2615801],
    ],
    "rockridge": [
        [37.83152, -122.241879],
        [37.852126, -122.25788],
    ],
    # Palo Alto
    "palo_alto": [
        [37.285346, -122.086779],
        [37.465541, -122.202476]
    ],
    # San Francisco
    "presidio": [
        [37.786864, -122.446231],
        [37.811085, -122.486143]
    ],
    "SoMa": [
        [37.765931, -122.381456],
        [37.7957, -122.42338]
    ]
}
NEIGHBORHOODS = [
    "berkeley",
    "castro valley",
    "mountain view",
    "adams point",
    "rockridge",
    "palo alto",
    "presidio",
    "soma"
]

## Transit
MAX_TRANSIT_DIST = 2.0 # miles

BART_STATIONS = {
    "12th Street Oakland City Center": [37.8036850,-122.2753400],
    "16th Street Mission": [37.7647994,-122.4199957],
    "19th Street Oakland": [37.8083586,-122.2686038],
    "24th Street Mission": [37.7524763,-122.4181457],
    "Ashby": [37.8528068,-122.2700628],
    "Balboa Park": [37.7215968,-122.4475110],
    "Bay Fair": [37.6969754,-122.1265806],
    "Downtown Berkeley": [37.8700973,-122.2681471],
    "Castro Valley": [37.6916248,-122.0749329],
    "Civic Center / UN Plaza": [37.7797560,-122.4141500],
    "Coliseum": [37.7536684,-122.1968981],
    "Colma": [37.6846380,-122.4662329],
    "Concord": [37.9743593,-122.0291856],
    "Daly City": [37.7063632,-122.4692604],
    "Dublin / Pleasanton": [37.7016504,-121.8991813],
    "El Cerrito del Norte": [37.9251091,-122.3168014],
    "El Cerrito Plaza": [37.9026314,-122.2989344],
    "Embarcadero": [37.7929053,-122.3970590],
    "Fremont": [37.5574675,-121.9766338],
    "Fruitvale": [37.7748353,-122.2241824],
    "Glen Park": [37.7330628,-122.4338194],
    "Hayward": [37.6697902,-122.0870089],
    "Lafayette": [37.8933044,-122.1241744],
    "Lake Merritt": [37.7970303,-122.2651829],
    "MacArthur": [37.8290643,-122.2670469],
    "Millbrae": [37.6002710,-122.3867068],
    "Montgomery Street": [37.7891308,-122.4019352],
    "North Berkeley": [37.8739774,-122.2834016],
    "North Concord / Martinez": [38.0032052,-122.0246558],
    "Oakland International Airport": [37.7115990,-122.2121336],
    "Orinda": [37.8783600,-122.1837993],
    "Pittsburg / Bay Point": [38.0189159,-121.9451328],
    "Pleasant Hill / Contra Costa Centre": [37.9286752,-122.0557081],
    "Powell Street": [37.7844688,-122.4079864],
    "Richmond": [37.9368334,-122.3531738],
    "Rockridge": [37.8447023,-122.2513920],
    "San Bruno": [37.6389595,-122.4170387],
    "San Francisco International Airport": [37.6213129,-122.3789554],
    "San Leandro": [37.7219501,-122.1608552],
    "South Hayward": [37.6343602,-122.0572010],
    "South San Francisco": [37.6642461,-122.4439623],
    "Union City": [37.5901744,-122.0169412],
    "Walnut Creek": [37.9055234,-122.0675267],
    "West Dublin / Pleasanton": [37.6997562,-121.9282402],
    "West Oakland": [37.8048733,-122.2951395]
}

## System Settings
SLACK_CHANNEL  = "#hoodhunting"
SLEEP_INTERVAL = 20 * 60

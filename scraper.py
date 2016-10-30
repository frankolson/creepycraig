#
# File for the main scraper
#
from slackclient import SlackClient
from craigslist import CraigslistHousing, CraigslistForSale
from util import in_box, in_hood, coord_distance, post_apartment_to_slack, post_car_to_slack
from databases import ApartmentListing, CarListing, apartment_session, car_session
import Settings.apartments as apartment_settings
import Settings.cars as car_settings

from dateutil.parser import parse
import time
import sys


## Scrape a particular for cars
def scrape_car_area(area, slack_client):
    cl = CraigslistForSale( site=car_settings.SITE, area=area, category='cto',
                            filters={
                                'query':     car_settings.QUERY,
                                'max_price': car_settings.MAX_PRICE,
                                'min_price': car_settings.MIN_PRICE,
                                'max_miles': car_settings.MAX_MILES
                            })
    results = cl.get_results(sort_by='newest', limit=20)

    for result in results:
        # check if the result is already in the db
        car_listing = car_session.query(CarListing).filter_by(cl_id=result["id"]).first()

        # Don't store the apartment_listing if it already exists.
        if car_listing is None:
            # Create the apartment_listing object
            car_listing = ApartmentListing(
                area      = area,
                cl_id     = int(result["id"]),
                created   = parse(result["datetime"]),
                link      = result["url"],
                location  = result["where"],
                name      = result["name"],
                price     = float(result["price"].replace("$", ""))
            )

            # save apartment_listing to db
            car_session.add(car_listing)
            car_session.commit()

            # post to slack
            post_car_to_slack(slack_client, car_listing)


## Scrape a particular area for places to live
def scrape_living_area(area, rooms, ceiling, slack_client):
    cl = CraigslistHousing( site=apartment_settings.SITE, area=area, category='apa',
                            filters={
                                'max_price': ceiling,
                                'min_price': apartment_settings.MIN_PRICE,
                                'bedrooms' : rooms
                            })

    results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

    for result in results:
        # check if the result is already in the db
        apartment_listing = apartment_session.query(ApartmentListing).filter_by(cl_id=result["id"]).first()

        # Don't store the apartment_listing if it already exists.
        if apartment_listing is None:
            # Neighborhood variables
            geotag   = result["geotag"]
            location = result["where"]
            area     = ""

            # Transit variables
            min_dist    = None
            near_bart   = False
            bart_dist   = "N/A"
            station_msg = ""
            bart        = ""

            # Neighborhood check
            if geotag is not None:
                for a, coords in apartment_settings.BOXES.items():
                    if in_box(geotag, coords):
                        area = a

            if (len(area) == 0) and (location is not None):
                area = in_hood(location, apartment_settings.NEIGHBORHOODS)

            if (len(area) != 0) and (geotag is not None):
                # Transit check
                for station, coords in apartment_settings.BART_STATIONS.items():
                    dist = coord_distance(coords, geotag)
                    if (min_dist is None or dist < min_dist) and dist < apartment_settings.MAX_TRANSIT_DIST:
                        bart = station
                        near_bart = True

                    if (min_dist is None or dist < min_dist):
                        min_dist = dist
                        bart_dist = dist

                # Try parsing the price.
                price = 0
                try:
                    price = float(result["price"].replace("$", ""))
                except Exception:
                    pass

                # Create the apartment_listing object
                apartment_listing = ApartmentListing(
                    area      = area,
                    bart_dist = bart_dist,
                    bart_stop = bart,
                    cl_id     = int(result["id"]),
                    created   = parse(result["datetime"]),
                    latitutde = geotag[0],
                    link      = result["url"],
                    location  = location,
                    longitude = geotag[1],
                    name      = result["name"],
                    near_bart = near_bart,
                    price     = price
                )

                # save apartment_listing to db
                apartment_session.add(apartment_listing)
                apartment_session.commit()

                # post to slack
                post_apartment_to_slack(slack_client, apartment_listing, rooms)

def scrape_craigslist(search_type):
    # Setup Slack client
    slack_client = SlackClient(apartment_settings.SLACK_TOKEN)

    if search_type == "hoodlum":
        # loop over all selected craigslist areas
        for area in apartment_settings.AREAS:
            for rooms, ceiling in apartment_settings.CEILINGS.iteritems():
                scrape_living_area(area, rooms, ceiling, slack_client)
    elif search_type == "rider":
        # loop over all selected craigslist areas
        for area in car_settings.AREAS:
            scrape_car_area(area, slack_client)
    else:
        print "\nImpropper Scrape type. Please use either 'hoodlum' or 'rider'. "
        print "Exiting...."
        sys.exit(1)

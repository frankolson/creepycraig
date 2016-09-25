#
# File for the main scraper
#
from slackclient import SlackClient
from craigslist import CraigslistHousing
import settings
from util import in_box, in_hood,coord_distance,post_to_slack

# Setup Slack client
slack_client = SlackClient(settings.SLACK_TOKEN)

for area in settings.AREAS:
    cl = CraigslistHousing( site=settings.SITE, area=area, category='apa',
                            filters={
                                'max_price': settings.MAX_PRICE,
                                'min_price': settings.MIN_PRICE
                            })

    results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

    for result in results:
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
            for a, coords in settings.BOXES.items():
                if in_box(geotag, coords):
                    area = a

        if (len(area) == 0) and (location is not None):
            area = in_hood(location, settings.NEIGHBORHOODS)

        if (len(area) != 0) and (geotag is not None):
            # Transit check
            for station, coords in settings.BART_STATIONS.items():
                dist = coord_distance(coords, geotag)
                if (min_dist is None or dist < min_dist) and dist < settings.MAX_TRANSIT_DIST:
                    bart = station
                    near_bart = True

                if (min_dist is None or dist < min_dist):
                    min_dist = dist
                    bart_dist = dist
            listing = {
                # Neighborhood variables
                "area": area,
                "link": result["url"],
                "name": result["name"],
                "price": result["price"],
                # Transit variables
                "near_bart": near_bart,
                "bart_dist": bart_dist,
                "bart": bart
            }

            # post to slack
            post_to_slack(slack_client, listing)

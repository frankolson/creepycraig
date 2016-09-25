#
# File for the main scraper
#

from craigslist import CraigslistHousing
import settings
from util import in_box, in_hood

for area in settings.AREAS:
    cl = CraigslistHousing( site=settings.SITE, area=area, category='apa',
                            filters={
                                'max_price': settings.MAX_PRICE,
                                'min_price': settings.MIN_PRICE
                            })

    results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

    for result in results:
        geotag   = result["geotag"]
        location = result["where"]
        area     = ""

        if geotag is not None:
            for a, coords in settings.BOXES.items():
                if in_box(geotag, coords):
                    area = a

        if len(area) == 0:
            area = in_hood(location, settings.NEIGHBORHOODS)

        if len(area) != 0:
            print area + "("+ result["price"] +"): " + result["name"]

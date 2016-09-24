#
# File for the main scraper
#

from craigslist import CraigslistHousing
import settings
import util

for area in settings.AREAS:
    cl = CraigslistHousing( site=settings.SITE, area=area, category='apa',
                            filters={
                                'max_price': settings.MAX_PRICE,
                                'min_price': settings.MIN_PRICE
                            })

    results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

    for result in results:
        geotag = result["geotag"]
        if geotag != None:
            for a, coords in settings.BOXES.items():
                if util.in_box(geotag, coords):
                    print a + "("+ result["price"] +"): " + result["name"]

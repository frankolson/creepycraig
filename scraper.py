#
# File for the main scraper
#

from craigslist import CraigslistHousing
import settings
import util

for area in settings.AREAS:
    print "searching " + area
    cl = CraigslistHousing( site=settings.SITE, area=area, category='apa',
                            )

    results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

    for result in results:
        geotag = result["geotag"]
        print geotag
        if geotag != None:
            for coords in settings.BOXES.items():
                if util.in_box(geotag, coords):
                    print result["name"]

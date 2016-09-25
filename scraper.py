#
# File for the main scraper
#
from slackclient import SlackClient
from craigslist import CraigslistHousing
from util import in_box, in_hood,coord_distance,post_to_slack
import settings

from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

## setup SQLite
engine = create_engine('sqlite:///listings.db', echo=False)
Base = declarative_base()

## Listing DB Model
class Listing(Base):
    __tablename__ = 'listings'

    id        = Column(Integer, primary_key=True)
    area      = Column(String)
    bart_stop = Column(String)
    cl_id     = Column(Integer, unique=True)
    created   = Column(DateTime)
    geotag    = Column(String)
    latitutde = Column(Float)
    link      = Column(String, unique=True)
    location  = Column(String)
    longitude = Column(Float)
    name      = Column(String)
    price     = Column(Float)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

## Setup Slack client
slack_client = SlackClient(settings.SLACK_TOKEN)

## Scrape a particular area
def scrape_area(area):
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

def scrape_craigslist():
    for area in settings.AREAS:
        scrape_area(area)

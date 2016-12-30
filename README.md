# Creepy Craig
_A spider on the wonderful web of craigslist_

based on the [this tutorial](https://www.dataquest.io/blog/apartment-finding-slackbot/)

### Files

1. main_loop.py ~ The big guy calling the shots
2. util.py ~ filtering functions
3. secret.py ~ all of the secretness for the api keys!!!
  * `SLACK_TOKEN`
3. Settings
  1. apartments.py ~ preferences that make for a sick pad
    * Price:
      * `MAX_PRICE`
      * `MIN_PRICE`
      * `CEILINGS`
    * Location:
      * `SITE`
      * `AREAS`
      * `BOXES`
      * `NEIGHBORHOODS`
    * Transit:
      * `MAX_TRANSIT_DIST`
      * `BART_STATIONS`
    * System:
      * `SLACK_CHANNEL`
      * `SLEEP_INTERVAL`
  2. cars.py ~ preferences that make for a sick ride
    * Price:
      * `MAX_PRICE`
      * `MIN_PRICE`
      * `MAX_MILES`
    * Location:
      * `SITE`
      * `AREAS`
    * System:
      * `SLACK_CHANNEL`
      * `SLEEP_INTERVAL`
4. scraper.py ~ the clever one doing the searching

### Dependencies

* `sqlalchemy`
* `python-craigslist`
* `slackclient`
* `python-dateutil`

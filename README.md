# Hood Hunting
_Gotta find me a place to live!_

based on the [this tutorial](https://www.dataquest.io/blog/apartment-finding-slackbot/)

### Files

1. main_loop.py ~ The big guy calling the shots
2. util.py ~ filtering functions
3. secret.py ~ all of the secretness for the api keys!!!
  * `SLACK_TOKEN`
3. settings.py ~ preferences that make for a sick pad
  * Price:
    * `MAX_PRICE`
    * `MIN_PRICE`
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
4. scraper.py ~ the clever one doing the searching

### Dependencies

* `sqlalchemy`
* `python-craigslist`
* `slackclient`

from scraper import scrape_craigslist
import settings
import time
import sys
import traceback

if __name__ == "__main__":
    while True:
        # scrape time
        print "%s: Starting scrape cycle" % time.ctime()
        try:
            scrape_craigslist()
        except KeyboardInterrupt:
            print "Exiting...."
            sys.exit(1)
        except Exception as exc:
            print "Error with the scraping: %s" % sys.exc_info()[0]
            traceback.print_exc()
        else:
            print "%s: Successfully finished scraping" % time.ctime()

        # Sleep time
        try:
            time.sleep(settings.SLEEP_INTERVAL)
        except KeyboardInterrupt:
            print "Exiting...."
            sys.exit(1)
        except Exception as exc:
            print "Error with the sleeping: %s" % sys.exc_info()[0]
            traceback.print_exc()

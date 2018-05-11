#Joseph Malafronte
#Web Scraper for BoA to find balance information for bank accounts
#For personal non-profit use only

import time


while(1):

	#Need to add multiprocess support here
	exec(open("./cryptoParser.py").read())
	exec(open("./boaParser2.py").read())
	time.sleep(3800)

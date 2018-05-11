#Joseph Malafronte
#Simple python program that calls cryptoParser.py and boaParser2.py every 30 minutes
#For personal non-profit use only

import time

while(1):

	#Need to add multiprocess support here
	exec(open("./cryptoParser.py").read())
	exec(open("./boaParser2.py").read())
	time.sleep(3800)



import shutil
import os
import glob
import time

opCount = 0
firstRun = 1

while(1):
	time.sleep(.5)

	logfile = ""
	txtfile = ""

	# Need to get the latest log
	#list_of_files = glob.glob("/Users/josephmalafronte/Library/Application Support/Google/Chrome/Default/Local Storage/*")
	dirLoc = "/Users/josephmalafronte/Library/Application Support/Google/Chrome/Default/Local Storage/leveldb/"
	for file in os.listdir(dirLoc):
		if file.endswith(".log"):
			logfile = dirLoc + file
			txtfile = logfile.replace(".log",".txt")


	#logfile = "/Users/josephmalafronte/Library/Application Support/Google/Chrome/Default/Local Storage/leveldb/013647.log"
	#txtfile = "/Users/josephmalafronte/Library/Application Support/Google/Chrome/Default/Local Storage/leveldb/013647.txt"

	if(os.path.isfile(txtfile)):
		os.remove(txtfile)

	shutil.copy(logfile, txtfile)

	with open(txtfile, encoding="utf8", errors='ignore') as f:
		contents = f.read()
	#print(contents)

	numOcc = contents.count("Trigger")
	print("Num Triggers: " + str(numOcc))
	if firstRun == 1:
		opCount = contents.count("Trigger")
		firstRun = 0
	elif numOcc > opCount:
		print("Run")
		opCount = numOcc;


	"""
	triggerString = "Trigger" + str(opNumber)

	if triggerString in contents:
		print("Run")
		opNumber += 1

	"""
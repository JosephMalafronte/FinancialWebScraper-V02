#Joseph Malafronte
#Simple python program that calls cryptoParser.py and boaParser2.py every 30 minutes
#For personal non-profit use only

import time
import sys
from tkinter import *
from threading import Thread


def activateCrypto():
	exec(open("./cryptoParser.py").read())

def runCrypto():
	thread = Thread(target = activateCrypto)
	thread.start()
	thread.join()

def activateBoa():
	exec(open("./boaParser2.py").read())

def runBoa():
	thread = Thread(target = activateBoa)
	thread.start()
	thread.join()

def runAll():
	thread = Thread(target = activateCrypto)
	thread2 = Thread(target = activateBoa)
	thread.start()
	thread2.start()
	thread.join()
	thread2.join()

def endProgram():
	sys.exit()


#Create a window
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Run Crypto", fg="blue", command=runCrypto)
button2 = Button(topFrame, text="Run BoA", fg="green", command=runBoa)
button3 = Button(topFrame, text="Run All", fg="purple", command=runAll)
endButton = Button(bottomFrame, text="End Program", fg="red", command=endProgram)

button1.pack()
button2.pack()
button3.pack()
endButton.pack()



root.mainloop()



"""
while(1):

	#Need to add multiprocess support here
	exec(open("./cryptoParser.py").read())
	exec(open("./boaParser2.py").read())
	time.sleep(3800)
"""

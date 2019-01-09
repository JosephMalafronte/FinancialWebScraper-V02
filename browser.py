#!/usr/bin/env python

#Joseph Malafronte
#Web Scraper Browser

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl, pyqtSlot
from output import Ui_Form
from boaParser2 import run
from cryptoParser import runCrypto
import threading



def callback():
	print("Finished")


class MainWindow(QWidget, Ui_Form):   
	def __init__(self, parent=None):     
		super(MainWindow, self).__init__(parent)     
		self.setupUi(self)     
		self.resize(2280,1520)
		self.bankButton.clicked.connect(self.bankPressed)  
		self.cryptoButton.clicked.connect(self.cryptoPressed)  
		self.webEngineView.setUrl(QUrl("https://docs.google.com/spreadsheets/d/1c1-Z0IoB9g9P4c5TYpUkfbB72C8BonESutVlHNrfrJk/edit?usp=drive_web&ouid=106012828270060555110")) 
	def bankPressed(self): 
		thr = threading.Thread(target=run, args=(), kwargs={})
		thr.start()
	def cryptoPressed(self): 
		thr = threading.Thread(target=runCrypto, args=(), kwargs={})
		thr.start()



app = QApplication(sys.argv)
view = MainWindow()
view.show()
app.exec()
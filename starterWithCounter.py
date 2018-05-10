#Joseph Malafronte
#Web Scraper for BoA to find balance information for bank accounts
#For personal non-profit use only

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gspread
from oauth2client.service_account import ServiceAccountCredentials



#Access Google Sheet For Editing
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Finances').sheet1

counter = sheet.cell(80,3).value



while(1):
	#time.sleep(5)
	newValue = sheet.cell(80,3).value

	if(newValue != counter) : 
		counter = newValue
		exec(open("./boaParser2.py").read())

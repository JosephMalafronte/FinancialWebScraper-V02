#Joseph Malafronte
#Web Scraper for Crypto Currencies to find current value of owned coins
#Place coin values in Google Sheets Spreadsheet using Google API
#For personal non-profit use only


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import gspread
from oauth2client.service_account import ServiceAccountCredentials



print("Updating Cryptos...")


#Access coinmarketcap website for information
my_url = 'https://coinmarketcap.com/exchanges/binance/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser") 


#Access Google Sheet For Editing
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet1 = client.open('Finances')
sheet = sheet1.get_worksheet(1)





#grabs each product places into array
containers = page_soup.findAll("tr", {"class","ng-scope"})

table1 = page_soup.find("table", id="exchange-markets")

table2 = table1.find('tbody')
table3 = table2.findAll('tr')



#Go through spreadsheet for list of coins owned
#Add each coin to array
coinsOwned = []
i = 7
for i in range(7,12):
	insValue = sheet.cell(i,1).value
	if(insValue != ""): coinsOwned.append(insValue)




for container in table3:
	name_container = container.findAll("td")
	coinName = name_container[2].a.text.strip()
	coinValue = name_container[4].span.text.strip()


	if(coinName in coinsOwned):
		#Ew hardcode fix later
		if(coinName == "VEN/ETH"):
			sheet.update_cell(10,5, coinValue)
		elif(coinName == "NANO/ETH"):
			sheet.update_cell(9,5, coinValue)
		elif(coinName == "XRP/ETH"):
			sheet.update_cell(8,5, coinValue)
		elif(coinName == "ETH/BTC"):
			sheet.update_cell(12,5, coinValue)

	
print("Cryptos Updated")
	




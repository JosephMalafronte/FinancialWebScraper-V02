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



class cryptoInfo:
	name = ""
	col = 0

#Go through spreadsheet for list of coins owned
#Add each coin to array
coinsOwned = []
coinNames = []
i = 7
for i in range(7,12):
	ins = cryptoInfo()
	ins.name = sheet.cell(i,1).value
	ins.col = i
	if(ins.name != ""): 
		coinsOwned.append(ins)
		coinNames.append(ins.name)




for container in table3:
	#Get info
	name_container = container.findAll("td")
	coinName = name_container[2].a.text.strip()
	coinValue = name_container[4].span.text.strip()


	for x in coinsOwned:
		if(x.name==coinName):
			sheet.update_cell(x.col,5, coinValue)



#Record Value of New Crypto Balance
newValue = sheet.cell(22,5).value
row = int(sheet.cell(50,12).value)
date = sheet.cell(51,12).value
lastDate = sheet.cell(row-1,13).value
if(date == lastDate):
	row = row-1
newRow = row+1
sheet.update_cell(row,14, str(newValue))
sheet.update_cell(row,13, date)
sheet.update_cell(50,12, str(newRow))

	
print("Cryptos Updated")
	

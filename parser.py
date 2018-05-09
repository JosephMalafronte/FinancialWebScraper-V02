#Joseph Malafronte
#Web Scraper 1


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser") 


filename = "products.csv"
f = open(filename, "w")

headers = "brand, productName, shipping\n"

f.write(headers)


#grabs each product places into array
containers = page_soup.findAll("div", {"class","item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class","item-title"})
	productName = title_container[0].text.strip()
	shippingPriceC = container.findAll("li", {"class","price-ship"})
	shippingPrice = shippingPriceC[0].text.strip()

	print("Brand: " + brand)
	print("Product Name: " + productName)
	print("Shipping Price" + shippingPrice)

	f.write(brand + "," + productName.replace(",", "|") + "," + shippingPrice +"\n")


f.close()
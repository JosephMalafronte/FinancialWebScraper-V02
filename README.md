FinancialWebScraper-V02
By Joseph Malafronte
Last Updated: May 10th 2018


Financial Web Scraper I created to automatically update a Google spreadsheet with the current balance of my bank accounts as well as the current value of Crypto Currencies I own.

cryptoParser.py is the program for pulling in updated Crypto prices.
boaParser2.py is the program for pulling in my updated Bank Balances.
starter.py is a program that runs both of these programs every 30 minutes.

All passwords used to access websites for scraping are accessed using the keyring Python library so that it can only be accesssed from my personal laptop using the Mac Keychain Access backend. 

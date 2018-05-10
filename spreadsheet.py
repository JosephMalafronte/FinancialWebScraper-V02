import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('Finances').sheet1

sheet.update_cell(38,5, "$433")


result = sheet.row_values(6)
pp = pprint.PrettyPrinter()
pp.pprint(result)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import bs4
import requests
from bs4 import BeautifulSoup
# api configuration 

scope = ['https://www.googleapis.com/auth/drive']
credantials = ServiceAccountCredentials.from_json_keyfile_name('stockupdation-f8b999b001f4.json', scope)
client = gspread.authorize(credantials)
# accessing google sheet 'stocks'

sheet = client.open('stocks').sheet1
#pprint is imported to print data clearly or neatly

pp = pprint.PrettyPrinter()
#accessing column "2" to spreadsheet which is symbols 

stock_data = sheet.col_values(2)
stock_list = []
# appending data from column "2" to stock_list

for i in stock_data:
    stock_list.append(i)
pp.pprint(stock_data)
# removing header of column

refined = stock_list.pop(0)
#print(stock_list)

share_price = []
def price():    
    for i in stock_list:
        print(i)
        nse = requests.get(f'https://in.finance.yahoo.com/quote/{i}.NS?p={i}.NS')
        bse = requests.get(f"https://in.finance.yahoo.com/quote/{i}.BO?p={i}.BO")
        if nse:
           # drilling down to placeholder of current share price using BeautifulSoup
           soup = bs4.BeautifulSoup(ns.text,'html')
           stock_price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
           #printing current price of share_company
           print(stock_price)
           share_price.append(stock_price)
        else:
           soup = bs4.BeautifulSoup(bo.text,'html')
           stock_price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
           print(stock_price)
           share_price.append(stock_price)
    print(share_price)

price()

#updating googlesheet column  
def update():
    for i in range(len(share_price)):
           #updating each row of column 'E'
           sheet.update(f"E{i+2}",share_price[i])

update()


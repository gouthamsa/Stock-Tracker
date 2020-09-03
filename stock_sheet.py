import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import bs4
import requests
from bs4 import BeautifulSoup
# api configuration


# Finding stock price current values
def price(stock_list):    
    for stock in stock_list:
        print(stock)

        ns = requests.get(f'https://in.finance.yahoo.com/quote/{stock}.NS?p={stock}.NS')
        bo = requests.get(f"https://in.finance.yahoo.com/quote/{stock}.BO?p={stock}.BO")
        if ns:
           soup = bs4.BeautifulSoup(ns.text,'html')
           stock_price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
           print(stock_price)
           share_price.append(stock_price)
        else:
           soup = bs4.BeautifulSoup(bo.text,'html')
           stock_price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
           print(stock_price)
           share_price.append(stock_price)
    print(share_price)
    return share_price



# updating google sheets
def update(alphabet,share_price):
    for i in range(len(share_price)):
        sheet.update(f"{alphabet}{i+2}",share_price[i])

# Finding row alphabet value using header value of sheet
def find_header(header_values):
    for alphabet in range(len(header_values)):
       if header_values[alphabet] == "Current price":
          alpha = (chr(65 + alphabet))
          return alpha
       else:
           print("Current price Column not avaliable")  
        

if __name__ == "__main__":
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json.file, scope)
    client = gspread.authorize(creds)
# accessing google_sheet using file_name
    sheet = client.open('filename').sheet1
    pp = pprint.PrettyPrinter()
    stock_data = sheet.col_values(2)

    # Stock quotes list
    stock_list = []
    for i in stock_data:
        stock_list.append(i)
    pp.pprint(stock_data)
    #removing header
    refined = stock_list.pop(0)

    # Stock price Current value list  
    share_price = []
    
    price(stock_list)
    alpha = find_header(sheet.row_values(1))
    print(alpha)
    update(alpha,share_price)
    



from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

def is_good_response(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def get_data(url):
    with closing(get(url, stream=False)) as response:
        if is_good_response(response):
            return response.content
        else:
            return None

def get_clean_data(data):
    return str(data.text).replace('\n', '').strip()

class Stock:
    code = None
    roe = None
    pPv = None

# GET STOCK DATA
def set_stock_data(stockItem):
    raw_html = get_data('http://www.fundamentus.com.br/detalhes.php?papel={0}'.format(stockItem.code))
    html = BeautifulSoup(raw_html, 'html.parser')
    # Flags
    flagROE = False
    flagPVP = False
    # Scan
    for row in html.select('td'):
        data = row.find('span', {'class': 'txt'})
        if (data is not None):
            # ROE ===================================
            if (flagROE):
                stockItem.roe = get_clean_data(data)
                flagROE = False

            if (data.text.find('ROE') > -1):
                flagROE = True

            # P/PV ===================================
            if (flagPVP):
                stockItem.pPv = get_clean_data(data)
                flagPVP = False

            if (data.text.find('P/VP') > -1):
                flagPVP = True

# STOCKS LIST
stocksCode = ['PETR4','MRVE3', 'ITUB4']

for stockCodeItem in stocksCode:
    print(datetime.now().isoformat() + ' - waiting to start: ' + stockCodeItem)                
    sleep(8)

    stock = Stock
    stock.code = stockCodeItem
    set_stock_data(stock)
    print(stock.code)
    print(stock.roe)
    print(stock.pPv)

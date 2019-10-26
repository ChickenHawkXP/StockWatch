import requests
import stockDB
from stockDB import getCols
import time
from lxml import html

walmart = getCols.walmart()
intel = getCols.intel()
microsoft = getCols.microsoft()
nvidia = getCols.nvidia()

def getNVDA():
    table = "NVIDIA"
    web = requests.get("https://finance.yahoo.com/quote/NVDA/")
    webtext = html.fromstring(web.content)
    if web.status_code == 200:
        print(time.strftime('%I:%M, %x'),"NVIDIA(NVDA): ")
        price = webtext.xpath('//span[@data-reactid="14"]/text()')
        pe = webtext.xpath('//span[@data-reactid="67"]/text()')
        div = webtext.xpath('//td[@data-test="DIVIDEND_AND_YIELD-value"]/text()')
        print("Closing Price:",price[0],", PE:",pe[0],", Annual Dividend:",div[0][:4])
        stockDB.addData(table,float(price[0]),str(pe[0]),div[0][:4])
    else:
        print("Could not make a connection to the website!")

def getMSFT():
    table = "MICROSOFT"
    web = requests.get("https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-tre-srch")
    webtext = html.fromstring(web.content)
    if web.status_code == 200:
        print(time.strftime('%I:%M, %x'),"Microsoft(MSFT): ")
        price = webtext.xpath('//span[@data-reactid="14"]/text()')
        pe = webtext.xpath('//span[@data-reactid="67"]/text()')
        div = webtext.xpath('//td[@data-test="DIVIDEND_AND_YIELD-value"]/text()')
        print("Closing Price:",price[0],", PE:",pe[0],", Annual Dividend:",div[0][:4])
        stockDB.addData(table,float(price[0]),str(pe[0]),div[0][:4])
    else:
        print("Could not make a connection to the website!")

def getWMT():
    table = "WALMART"
    web = requests.get("https://finance.yahoo.com/quote/WMT?p=WMT&.tsrc=fin-srch")
    webtext = html.fromstring(web.content)
    if web.status_code == 200:
        print(time.strftime('%I:%M, %x'),"Walmart(WMT): ")
        price = webtext.xpath('//span[@data-reactid="14"]/text()')
        pe = webtext.xpath('//span[@data-reactid="67"]/text()')
        div = webtext.xpath('//td[@data-test="DIVIDEND_AND_YIELD-value"]/text()')
        print("Closing Price:",price[0],", PE:",pe[0],", Annual Dividend:",div[0][:4])
        stockDB.addData(table,float(price[0]),str(pe[0]),div[0][:4])
    else:
        print("Could not make a connection to the website!")

def getINTC():
    table = "INTEL"
    web = requests.get("https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch")
    webtext = html.fromstring(web.content)
    if web.status_code == 200:
        print(time.strftime('%I:%M, %x'),"Intel(INTC): ")
        price = webtext.xpath('//span[@data-reactid="14"]/text()')
        pe = webtext.xpath('//span[@data-reactid="67"]/text()')
        div = webtext.xpath('//td[@data-test="DIVIDEND_AND_YIELD-value"]/text()')
        print("Closing Price:",price[0],", PE:",pe[0],", Annual Dividend:",div[0][:4])
        stockDB.addData(table,float(price[0]),str(pe[0]),div[0][:4])
    else:
        print("Could not make a connection to the website!")
while True:
    getNVDA()
    getMSFT()
    getWMT()
    getINTC()
    time.sleep(1800)

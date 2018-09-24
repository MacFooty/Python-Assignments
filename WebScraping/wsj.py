import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

tickers=['AAPL','NKE','NFLX','AMZN','MSFT']
base_url="https://quotes.wsj.com/"

stocks=[["Ticker","Current price","Price change since open(%)","Price change since open","Open","Prior open"]]



def connect(i):
	r=requests.get(base_url+i)
	content=r.content
	soup=BeautifulSoup(content,"html.parser")
	info=[i]
	info.append(soup.find(id="quote_val").text)
	info.append(soup.find(id="quote_changePer").text)
	info.append(soup.find(id="quote_change").text)
	soup=soup.find(class_="cr_compare_data").findAll(class_="data_data")
	info.append(soup[0].text)
	info.append(soup[1].next)
	return info

for i in tickers:
	a=connect(i)
	stocks.append(a)

df = pd.DataFrame(stocks)
df.to_csv('mycsv.csv', index=False, header=True)

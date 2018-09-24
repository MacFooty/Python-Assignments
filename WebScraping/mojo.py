import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

base_url='https://www.boxofficemojo.com/studio/'
r=requests.get(base_url)
content=r.content
soup=BeautifulSoup(content,"html.parser")
links=[]
for i in soup.findAll('a'):
	links.append(i.get('href'))

years=[i for i in links if('yearly&yr' in i)]
years=['https://www.boxofficemojo.com'+i for i in years]
years.append('https://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr=2018&p=.htm')

ans=[]

def foo(link):
	r=requests.get(link)
	content=r.content
	soup=BeautifulSoup(content,"html.parser")
	soup=soup.findAll('table')[3]
	table=soup.findAll('tr')
	table=table[1:]
	for i in range(len(table)):
		info=table[i].text.split('\n')
		ans.append(info)

for i in range(len(years)):
	foo(years[i])

df = pd.DataFrame(ans)
df.to_csv('my_csv.csv', index=False, header=False)




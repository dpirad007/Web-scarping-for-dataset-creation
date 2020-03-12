import requests

website_url=requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text

from bs4 import BeautifulSoup

soup =BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

my_table =soup.find('table',{'class':'wikitable sortable'})
link=my_table.findAll('a')

countries=[]

for country in link:
    countries.append(country.get('title'))

print(countries)

import pandas as pd

df=pd.DataFrame()

df['Country']=countries

print(df)
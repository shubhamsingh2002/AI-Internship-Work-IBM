from bs4 import BeautifulSoup
import requests

url ="https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

page = requests.get(url)


soup = BeautifulSoup(page.text,'html')

table = soup.find('table', class_ = "wikitable sortable sticky-header-multi sort-under jquery-tablesorter")

print(table)
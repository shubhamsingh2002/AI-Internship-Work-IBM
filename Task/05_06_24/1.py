from bs4 import BeautifulSoup
import requests

url ="https://results.eci.gov.in/PcResultGenJune2024/index.htm"
req = requests.get(url)

soup = BeautifulSoup(req.content,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.title)
import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'h3 > a'
    )

for title in my_titles:
    print(title.text)
    #print(title.get('href'))
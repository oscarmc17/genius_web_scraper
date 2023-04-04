import requests
from bs4 import BeautifulSoup

url = 'https://genius.com/albums/Tyler-the-creator/Call-me-if-you-get-lost-the-estate-sale'
html = requests.get(url)

# print(html)

soup = BeautifulSoup(html.content, 'html.parser')

lst = soup.find_all("h3", class_='chart_row-content-title')

print(lst)

# print(soup.prettify())

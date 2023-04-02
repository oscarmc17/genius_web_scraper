import requests
from bs4 import BeautifulSoup

url = 'https://genius.com/albums/Tyler-the-creator/Call-me-if-you-get-lost-the-estate-sale'
html = requests.get(url)

print(html)

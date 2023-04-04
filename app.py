import requests
from bs4 import BeautifulSoup

url = 'https://genius.com/albums/Tyler-the-creator/Call-me-if-you-get-lost-the-estate-sale'
html = requests.get(url)

# print(html)

soup = BeautifulSoup(html.content, 'html.parser')

tracks = soup.find_all(class_='chart_row-content-title')

count = 0
new = []

for song in tracks:
    # new.append(song)
    count += 1
    print("{}. {}".format(count, song.text.strip()))

import requests
from bs4 import BeautifulSoup

url = 'https://genius.com/albums/Tyler-the-creator/Call-me-if-you-get-lost-the-estate-sale'
html = requests.get(url)

# print(html)

soup = BeautifulSoup(html.content, 'html.parser')

tracks = soup.find_all('h3', {'class': 'chart_row-content-title'})
album_title = soup.find('h1', {
                        'class': 'header_with_cover_art-primary_info-title header_with_cover_art-primary_info-title--white'}).text
artist_name = soup.find(
    'a', {'class': 'header_with_cover_art-primary_info-primary_artist'}).text
release_date = soup.find('div', {'class': 'metadata_unit'}).text

count = 0

# print('\nArtist: {}'.format(artist_name.text))
# print("Album Name: {}".format(album_title.text))
# print(release_date)

print(f'\nArtist: {artist_name}\nAlbum Name: {album_title}\n{release_date}\n')

for i, title in enumerate(tracks, start=1):
    # Remove the "Lyrics" text from the track title
    title_text = title.text.strip().replace(' Lyrics', '')
    print(f"{i}. {title_text}")

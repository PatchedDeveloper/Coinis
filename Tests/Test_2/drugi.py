import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.realitica.com/'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

listings = soup.find_all('div', class_='thumb_div')

with open('realitica_listings.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Type', 'Area', 'Location', 'Bedrooms', 'Bathrooms', 'Price', 'Living Area', 'Land Area', 'Parking Spaces', 'Distance from Sea', 'New Construction', 'Air Conditioning', 'Title', 'Description', 'Website Link', 'Advertiser', 'Mobile Number', 'Ad Number/ID', 'Last Change', 'Images']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

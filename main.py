from cgitb import html
from email.mime import image
from unicodedata import name
import requests
from bs4 import BeautifulSoup as BS
import csv

def main():
    BASE_URL = 'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru' 
    html = get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)



def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_data(soup): 
    catalog = soup.find('div', class_='grid-list asdads')
    phones = catalog.find_all('div', class_= 'ty-column4') #####################################################
    for phone in phones:
        title = phone.find('a', class_='product-title').text
        # print(title)
        image = phone.find('img', class_='ty-pict').get('data-ssrc')
        # print(image)

        price = phone.find('span',class_= "ty-price-update").find('span').text
        # print(price)

        write_csv({
            'title' : title,
            'image' : image,
            'price' : price
        })
        

def write_csv(data): 
    with open('phones.csv', 'a') as file :
        names = ['title','price','image']
        write = csv.DictWriter(file,delimiter=',',fieldnames=names)
        write.writerow(data)


if __name__ == '__main__': 
    main()
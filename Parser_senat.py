
import requests
from  bs4  import  BeautifulSoup
import csv



URL = 'https://senatnn.ru/catalog/ukrasheniya/koltsa/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
           'accept': '*/*'}

HOST = 'https://senatnn.ru'
FILE = 'ring.csv'


def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS,params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html,'html.parser')
    pagination = soup.find_all('a', class_="")
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1





def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div',class_='senat-catalog-section-list')

    new = []


    for item in items:
        new.append({
            'id': item.find('span', class_='senat-item-articul').get_text().replace('Код: ',''),
            'title': item.find('a', class_='senat-item-title').get_text( strip=True),
            'price-old': item.find('span', class_='senat-item-price-old').get_text(strip=True).replace('₽','').replace(' ',''),
            'price-new': item.find('span', class_='senat-item-price-current').get_text(strip=True).replace('\xa0','').replace('₽','').replace(' ',''),
            'link': HOST + item.find('a', class_='senat-item-title').get('href'),
            'img': HOST + item.find('a', class_='senat-item-image-wrapper').find_next('img').get('src')
        })


    return new



def save_file(items,path):
    with open (path,'w',newline='',encoding="utf-8") as file:
        writer = csv.writer(file,delimiter=';')
        writer.writerow(['id','title','price_old','price_new','link','img'])
        for item in items:
            writer.writerow([item['id'],item['title'],item['price-old'],item['price-new'],item['link'],item['img']])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        ring = []
        pages_count = get_pages_count(html.text)
        for page in range(1,pages_count + 1):
            print(f'парсинг страницы {page} из {pages_count}')
            html = get_html(URL,params={'page':page})
            ring.extend(get_content(html.text))
        save_file(ring,FILE)
        print(ring)



    else:
        print('ERROR')

parse()


from datetime import datetime
import csv

import sqlite3
import readDB
import winsound

import requests
from bs4 import BeautifulSoup as BS

from rich import print

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
url = 'https://hi-tech.md'

page_cards = []

frequency = 2500
duration = 200

def get_html(url):
    try:
        request = requests.get(url=url, headers=headers)
        return request
    except:
        print(f'Сайт {url} не отвечает.\nПроверьте ссылку на корректность!')
        exit()


def get_link(html):
    soup = BS(html.text, 'html.parser')
    links = []

    items = soup.find_all('li', class_='ty-menu__item cm-menu-item-responsive')

    for item in items:
        links.append(item.find('a', class_='ty-menu__item-link').get('href'))

    return links


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper()


class Save:
    def __init__(self):
        self.conn = sqlite3.connect('myDatabase.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Cards
                        (id integer, title text, price integer, property_1 text, image_link text, prod_link text)
                        """)

    def SQL(self, items):
        for item in items:
            card = (item['id'],
                    item['title'],
                    item['price'],
                    item['property_1'],
                    item['image_link'],
                    item['prod_link'])

            self.cursor.execute("INSERT INTO Cards VALUES(?, ?, ?, ?, ?, ?)", card)
            self.conn.commit()


def save_csv(items, path):
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for item in items:
            writer.writerow([item['title'],
                             item['price'],
                             item['property_1'],
                             item['image_link'],
                             item['prod_link']])


def parse(html):
    soup = BS(html.text, 'html.parser')
    items = soup.find_all('div', class_='col-tile')

    cards = []
    f = 0

    try:
        for item in items:
            try:
                title = item.find('div', class_='ty-grid-list__item-name').find('a').get_text()
            except:
                title = '-'
            try:
                price = item.find('span', class_='ty-price-num').get_text()
            except:
                price = '-'
            try:
                property_1 = item.find('span', class_='ty-product-feature__label').find('em', class_='abt-yt-feature-name').get_text() + item.find('span', class_='ty-control-group').find('em', attrs={'class': None}).get_text()
            except:
                property_1 = '-'
            try:
                image_link = item.find('img', class_='ty-pict').get('data-src')
            except:
                image_link = '-'
            try:
                prod_link = item.find('a', class_='abt-single-image').get('href')
            except:
                prod_link = '-'

            cards.append({
                'id'        : f,
                'title'     : title,
                'price'     : price,
                'property_1': property_1,
                'image_link': image_link,
                'prod_link' : prod_link
            })
            f += 1
    except:
        print('\t\tКонец страницы')

    return cards


def main():
    request = get_html(url=url)
    links = []


    if request.status_code == 200:
        links = get_link(request)
    else:
        print('Сайт не отвечает.')
        return -1

    col = 1

    for link in links:
        page = 1
        new_url = url + link + 'page-' + str(page)  # https://hi-tech.md/bytovaya-tehnika/page-1/ - что получается
        print(f'[blue]{url+link}[/blue] [magenta]-> request()\t{col}/{len(links)}[/magenta]')       #log
        while True:
            time_start = datetime.now()
            time_end = datetime.now()
            try:
                time_start = datetime.now()
                request = get_html(new_url)
                time_end = datetime.now()
            except Exception as ex:
                print('Нет ответа, либо достигнут конец!')

            if request.status_code != 200:
                print(f'[magenta]page {page} [/magenta][bold red]PARSE -> BAD[/bold red]')
                print('Непредвиденная ошибка или конец страницы!')
                break
            elif request.status_code == 200:
                print(f'[magenta]page {page}[/magenta][green]\t\tPARSE -> GOOD[/green]\t\t[red]elapsed: '
                      f'{time_end -time_start}[/red]')
                cards = parse(html=request)
                # save_csv(cards, 'file.csv')
                save = Save()
                save.SQL(cards)

            page = page + 1
            new_url = url + link + 'page-' + str(page)
    readDB.main()


if __name__ == '__main__':
    winsound.Beep(frequency, duration)
    time_start_run = datetime.now()
    main()
    time_end_run = datetime.now()
    winsound.Beep(frequency, duration)
    print(f'Программа закончила работу.\nВремя выполнения составило{time_end_run-time_start_run}')
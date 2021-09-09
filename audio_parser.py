import requests
from bs4 import BeautifulSoup
import time
import os


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    songs = soup.find_all('a', class_='down')

    for song in songs:
       href = 'https:'+song.get('href')
       name = href.split('/')[5]
       print (name, href)
       command = 'wget ' + href
       os.system(command)
       time.sleep(5)



def main():
    pattern = 'https://page.ligaudio.ru/mp3/rozen%20maiden%20ost/{}'
    for i in range (1,6):
        url = pattern.format(str(i))
        get_data(get_html(url))
    #(get_html(url))


if __name__== '__main__':
    main()


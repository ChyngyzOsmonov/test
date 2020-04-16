import requests
from bs4 import BeautifulSoup
import threading

# veb_title = ''
# veb_text = ''
# veb_link = ''

#
# def send_vebinar():
#     global veb_title, veb_text, veb_link
#     threading.Timer(259200, send_vebinar).start()
url = 'http://santo-pharm.kg/news'

def get_html(url):
    r = requests.get(url)
    return r.text

# html = get_html('http://santo-pharm.kg/news')

# ########################################### 1 ##########################################################################

def vebinar_title(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        title = soup.find('div',
                         class_='last-news__right').find('div',
                         class_='news__right-item').find('h2').text.strip()
        return title
    except:
        title = ''


def vebinar_text(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        text = soup.find('div',
                         class_='last-news__right').find('div',
                         class_='news__right-item').find('p').text.strip()
        return text
    except:
        text = ''

def vebinar_link(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        link = soup.find('div',
                         class_='last-news__right').find('div',
                         class_='news__right-item').find('a', class_='btn-readmore').get('href')
        return link
    except:
        link = ''

    # veb_title = vebinar_title(html)
    # veb_text = vebinar_text(html)
    # veb_link = vebinar_link(html)


# send_vebinar()



import requests
from bs4 import BeautifulSoup

url = 'https://kaktus.media/'


def get_html(url):
    r = requests.get(url)
    return r.text


html = get_html(url)


def get_total(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('div',
                          class_='covid19-banner--info').find('div',
                                                              class_='covid19-banner--info-row').find('div',
                                                              class_='covid19-banner--info-row-value').text.strip()
        return total
    except:
        total = ''


total_not = get_total(html)

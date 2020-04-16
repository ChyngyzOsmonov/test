import requests
from bs4 import BeautifulSoup


# url = 'https://www.bbc.com/russian/news-51706538'

def get_html(url):
    r = requests.get(url)
    return r.text

# html = get_html('https://www.bbc.com/russian/news-51706538')



def get_total_world(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        total = soup.find('tr', class_='summary__body').find('td',
                                                             class_='summary__infected gel-double-pica').text.strip()
        died = soup.find('tr', class_='summary__body').find('td',
                                                            class_='summary__deceased gel-double-pica').text.strip()
        return '<b>В мире:</b>\nВыявлено всего: ' + total.replace('\xa0', ' ') + \
               '\n' + 'Умерло: ' + died.replace('\xa0', ' ')
    except:
        total = ''







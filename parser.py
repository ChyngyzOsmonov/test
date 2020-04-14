from bs4 import BeautifulSoup as BS
import requests


def get_html(url):
    result = requests.get(url)
    return result.text
html = get_html('https://kaktus.media/')

def get_data(html):
    try:
        soup = BS(html, 'lxml')
        li = soup.find('li', {'class': 'topic_item clearfix', 'data-num': '1'})
        span = li.find('span', {'class': 'n'})
        return (span.text)
    except:
        print('Parse error')


news_not = get_data(html)


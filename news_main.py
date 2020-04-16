import requests
from bs4 import BeautifulSoup


# url = 'https://kaktus.media/'


def get_html(url):
    r = requests.get(url)
    return r.text


# html = get_html('https://kaktus.media/')

# ########################################### 1 ##########################################################################
def get_news_1(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 1})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


#################################################### 2 ################################################################

def get_news_2(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 2})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


################################################ 3 ##################################################################

def get_news_3(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 3})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


#################################################### 4 ###############################################################

def get_news_4(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 4})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


################################################## 5 ###############################################################

def get_news_5(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 5})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


##################################################6##########################################################

def get_news_6(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', {'class': 'topic_list view_lenta 1'})
        li = ul.find('li', {'data-num': 6})
        div = li.find('div', {'class': 't f_medium'})
        a = div.find('a')
        span = a.find('span', {'class': 'n'})
        href = div.find('a').get('href')
        return span.text.strip() + '\n' + href
    except:
        span = ''


# get_news_1(html)
#
# get_news_2(html)
#
# get_news_3(html)
#
# get_news_4(html)
#
# get_news_5(html)
#
# get_news_6(html)


import urllib
import urllib2
import requests
from bs4 import BeautifulSoup

url = 'http://www.136book.com/huaqiangu/'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
data = {'type': 'txt'}

def get_content_by_request():
    return requests.get(url).content

def get_content_by_urllib():
    param = urllib.urlencode(data)
    req = urllib2.Request(url, param, head)
    response = urllib2.urlopen(req)
    return response.read()

if __name__ == '__main__':
    html = get_content_by_request()
    # html = get_content_by_urllib()
    soup = BeautifulSoup(html, 'lxml')
    soup_texts = soup.find('div', id = 'book_detail', class_= 'box1').find_next('div')
    f = open('story.txt','w')
    for link in soup_texts.ol.children:
        if link != '\n':
            download_url = link.a.get('href')
            download_response = urllib.urlopen(download_url)
            download_html = download_response.read()
            download_soup = BeautifulSoup(download_html, 'lxml')
            download_soup_texts = download_soup.find('div', id = 'content')
            download_soup_texts = download_soup_texts.text.encode('utf-8')
            f.write(link.text.encode('utf-8') + '\n\n')
            f.write(download_soup_texts[0:download_soup_texts.find('document.write', 1)])
            f.write('\n\n')
    f.close()
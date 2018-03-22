from functools import reduce
import requests
import re
import time
import codecs
import random
from bs4 import BeautifulSoup

URL = "http://www.todayim.cn/"
START_URL = "http://www.todayim.cn/news/show-28880.html"

HEADERS = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36', 'Cookie': '_lxsdk_cuid=15f41d6357ff-02c6f4e9d5508a-5b4a2c1d-100200-15f41d635809; _lxsdk=15f41d6357ff-02c6f4e9d5508a-5b4a2c1d-100200-15f41d635809; _hc.v="4870aa4b-fa82-4a9e-a296-d0992450f71e.1508638079"; JSESSIONID=763062B17E9D6E5E5EA651898462D8DA; aburl=1; cy=2; cye=beijing; _lxsdk_s=||0'},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
           {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'},
           {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
           {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
           {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
           {'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:28.0)Gecko/20100101 Firefox/28.0'},
           {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'},
           {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Connection': 'keep-alive'}]


def getData(url):
    headers = HEADERS[random.randint(0, len(HEADERS)-1)]
    data = requests.get(url, headers=headers).content
    return data


def parseData(data):
    time.sleep(1)
    soup = BeautifulSoup(data, 'html5lib')

    loc = soup.find('div', class_='fl news_menu_title').span.find_all('a')
    locStr = reduce(lambda x, y: x + '-' + y, map(lambda x: x.string, loc))

    title = soup.find('div', class_='fl show-title').h1.get_text()
    postTime = soup.find('span', class_='info-time').string
    commentNum = soup.find('span', class_='info-comm').string
    viewNum = soup.find('span', class_='info-view').string
    className = soup.find('p', class_='meta-info clear').string

    print(soup.find('p', class_='meta-info clear').get_text())


def main():
    url = START_URL
    nums = 1
    while url and nums <= 1:
        data = getData(url)
        print(nums)
        nums += 1

        parseData(data)


if __name__ == '__main__':

    main()

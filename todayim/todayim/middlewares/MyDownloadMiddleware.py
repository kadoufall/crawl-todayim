import time
import random
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

js = """
function scrollToBottom() {

    var Height = document.body.clientHeight,  
        screenHeight = window.innerHeight, 
        INTERVAL = 100,  
        delta = 500,  
        curScrollTop = 0;   

    var scroll = function () {
        curScrollTop = document.body.scrollTop;
        window.scrollTo(0,curScrollTop + delta);
    };

    var timer = setInterval(function () {
        var curHeight = curScrollTop + screenHeight;
        if (curHeight >= Height){  
            clearInterval(timer);
        }
        scroll();
    }, INTERVAL)
}
scrollToBottom()
"""

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


class MyDownloadMiddleware(object):

    @classmethod
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(HEADERS))

        '''
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        '''

        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument('--headless')
        firefoxOptions.add_argument('--disable-gpu')
        driver = webdriver.Firefox(firefox_options=firefoxOptions)

        #time.sleep(3)
        driver.set_script_timeout(20)
        driver.set_page_load_timeout(30)

        try:
            driver.get(request.url)
            #driver.execute_script(js)
        except TimeoutException:
            driver.execute_script('window.stop()')
        finally:
            content = driver.page_source.encode('utf-8')
            driver.quit()

        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)

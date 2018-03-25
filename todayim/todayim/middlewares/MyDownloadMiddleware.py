import time
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


class MyDownloadMiddleware(object):
    @classmethod
    def process_request(self, request, spider):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chromeOptions)

        #time.sleep(3)
        #driver.set_script_timeout(30)
        driver.set_page_load_timeout(30)

        try:
            driver.get(request.url)
            #driver.execute_script(js)
        except:
            pass
        finally:
            content = driver.page_source.encode('utf-8')
            driver.quit()

        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)

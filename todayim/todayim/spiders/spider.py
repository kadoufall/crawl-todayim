import scrapy
from scrapy import Request
from functools import reduce

from todayim.items import NewsItem

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TodayimSpider(scrapy.Spider):
    name = "todayim"
    allowed_domains = ['todayim.cn']

    def start_requests(self):

        urls = [
            # 政策
            #'http://www.todayim.cn/news/show-16315.html',
            #'http://www.todayim.cn/news/show-10975.html',
            #'http://www.todayim.cn/news/show-6510.html',
            #'http://www.todayim.cn/news/show-2641.html',

            # 观点
            #'http://www.todayim.cn/news/show-21013.html',
            #'http://www.todayim.cn/news/show-20965.html',
            #'http://www.todayim.cn/news/show-20929.html',
            #'http://www.todayim.cn/news/show-20509.html',
            #'http://www.todayim.cn/news/show-2544.html',

            # 新闻
            #'http://www.todayim.cn/news/show-28875.html',

            #'http://www.todayim.cn/news/3/10.html',
        ]

        '''
        for i in range(36, 226):
            urls.append('http://www.todayim.cn/news/3/'+str(i)+'.html')
        '''

        '''
        for i in range(126, 251):
            urls.append('http://www.todayim.cn/news/5/'+str(i)+'.html')
        '''

        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        #self.parsePage(response)

        urls = response.xpath(
            '/html/body/div[2]/div[3]/div[2]/div/ul/li/div[2]/div[1]/div[1]/a/@href')

        for url in urls:
            nextPassageUrl = 'http://www.todayim.cn' + url.extract()
            yield Request(url=nextPassageUrl, callback=self.parsePage)

        '''
        nextPassage = ''
        try:
            nextPassage = 'http://www.todayim.cn' + response.xpath('/html/body/div[4]/div[3]/div[2]/div[7]/div[1]/div/a/@href').extract()[0]
        except:
            pass
       

        if nextPassage != '':
            yield Request(url=nextPassage, callback=self.parse)
        '''

    def parsePage(self, response):
        url = response.url

        try:
            locAll = response.css(
                'body > div.main > div.news_menu > div.fl.news_menu_title > span > a')
            loc = reduce(lambda x, y: x + '-' + y,
                         map(lambda x: x.css('::text').extract_first(), locAll))
            title = response.css(
                'body > div.main > div.news-wrap > div.news-left > div.news-meta > div.fl.show-title > h1::text').extract_first()
            postTime = response.css(
                'body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-time::text').extract_first()
            commentNum = response.css(
                'body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-comm::text').extract_first()
            viewNum = response.css(
                'body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-view::text').extract_first()
            className = response.xpath(
                '/html/body/div[4]/div[3]/div[2]/div[1]/p/text()').extract()[3].strip()
            passageContent = response.xpath(
                '//*[@id="Div1"]')[0].xpath('string(.)').extract()[0].strip()

            news = NewsItem()
            news['url'] = url
            news['loc'] = loc
            news['title'] = title
            news['postTime'] = postTime
            news['commentNum'] = commentNum
            news['viewNum'] = viewNum
            news['className'] = className
            news['passageContent'] = passageContent

            #print(news)

            yield news
        except:
            pass

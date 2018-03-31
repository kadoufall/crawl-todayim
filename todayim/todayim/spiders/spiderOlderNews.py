import scrapy
from scrapy import Request
from functools import reduce

from todayim.items import NewsItem

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OlderNewsSpider(scrapy.Spider):
    name = "olderNews"
    allowed_domains = ['todayim.cn']

    def start_requests(self):

        urls = [
            # "http://www.todayim.cn/news/show-20422.html",
        ]
        
        for i in range(493, 494):
            urls.append('http://www.todayim.cn/news/1/'+str(i)+'.html')

        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath(
            '/html/body/div[2]/div[3]/div[2]/div/ul/li/div[2]/div[1]/div[1]/a/@href')

        for url in urls:
            nextPassageUrl = 'http://www.todayim.cn' + url.extract()
            yield Request(url=nextPassageUrl, callback=self.parsePage)

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

            print(news['url'])
            yield news
        except:
            pass

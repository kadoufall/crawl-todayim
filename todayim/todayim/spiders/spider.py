import scrapy
from scrapy import Request
from functools import reduce

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TodayimSpider(scrapy.Spider):
    name = "todayim"
    num = 0

    def start_requests(self):
        urls = [
            'http://www.todayim.cn/news/show-28880.html',
        ]

        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):


        locAll = response.css('body > div.main > div.news_menu > div.fl.news_menu_title > span > a')
        loc = reduce(lambda x, y: x + '-' + y, map(lambda x: x.css('::text').extract_first(), locAll))

        commentNum = response.css('body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-comm::text').extract_first()
        title = response.css('body > div.main > div.news-wrap > div.news-left > div.news-meta > div.fl.show-title > h1::text').extract_first()
        postTime = response.css('body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-time::text').extract_first()
        viewNum = response.css('body > div.main > div.news-wrap > div.news-left > div.news-meta > p > span.info-view::text').extract_first()
        className = response.xpath('/html/body/div[4]/div[3]/div[2]/div[1]/p/text()').extract()[3].strip()

        passageContent = response.xpath('//*[@id="Div1"]')[0].xpath('string(.)').extract()[0].strip()

        nextPassage = 'http://www.todayim.cn' + response.xpath('/html/body/div[4]/div[3]/div[2]/div[7]/div[1]/div/a/@href').extract()[0]

        print(loc)
        print(commentNum)
        print(title)
        print(postTime)
        print(viewNum)
        print(className)
        print(passageContent)
        print(nextPassage)

        self.num += 1

        #self.log('Saved file %s'% filename)

        if nextPassage and self.num <= 3:
            yield Request(url = nextPassage, callback=self.parse)
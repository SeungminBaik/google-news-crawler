# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from googlenewsen.items import GooglenewsenItem

class GoogleSpider(scrapy.Spider):
    name = "googlenews"
    allowed_domains = ["news.google.co.kr"]
    start_urls = [
        "https://news.google.co.kr/news?hl=en&tab=nn&edchanged=1&ned=us&authuser=0"
    ]

    #now each 'title','image','desc' is printed in groups(clusters)
    #operation of dividing them into line by line in one cluster is needed

    def parse(self, response):
        items = []
        for sel in response.xpath('//ul/li'):
            item = GooglenewsenItem()
            item['title'] = sel.xpath('//span[contains(@class,"titletext")]/text()').extract()
            item['image'] = sel.xpath('//div[contains(@class,"esc-thumbnail-image")]/img/@src').extract()
            item['desc'] = sel.xpath('//div[contains(@class,"esc-lead-snippet-wrapper")]/text()').extract()
            yield item
            items.append(item)

        for item in items:
            with open('googlenews.txt', 'a') as f:
                f.write('Title : {0}, image link : {1}, descriptions : {2}\n'.format(item['title'], item['image'], item['desc']))
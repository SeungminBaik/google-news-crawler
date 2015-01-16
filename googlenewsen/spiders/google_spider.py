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
        "https://news.google.co.kr/news?hl=en"
    ]

    #now each 'title','image','desc' is printed in groups(clusters)
    #operation of dividing them into line by line in one cluster is needed

    def parse(self, response):
        items = []
        for table in response.xpath('//table[@class="esc-layout-table"]'):
            item = GooglenewsenItem()
            item['title'] = table.xpath('.//div[@class="esc-lead-article-title-wrapper"]//span[@class="titletext"]/text()').extract()
            item['image'] = table.xpath('.//img[@class="esc-thumbnail-image"]/@src').extract()
            item['desc'] = table.xpath('.//div[@class="esc-lead-snippet-wrapper"]/text()').extract()
            yield item
            items.append(item)

        for item in items:
            with open('googlenews.txt', 'a') as f:
                f.write('Title : {0}\nImage : {1}\nDesc : {2}\n\n'.format(item['title'], item['image'], item['desc']))
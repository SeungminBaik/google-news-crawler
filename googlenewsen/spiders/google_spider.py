# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from googlenewsen.items import GooglenewsenItem

class GoogleSpider(scrapy.Spider):
    name = "googlenews"
    allowed_domains = ["news.google.co.kr"]
    print "Choose the Topic you want to Crawl:\n"
    print "Top Stories[Nothing] World[w] U.S[n] Business[b] Technology[tc] \n"
    print "Entertainment[e] Sports[s] Sceince[snc] Health[m] Spotlight[ir] \n"
    topic = input()

    if topic is '':
        start_urls = [
        "https://news.google.co.kr/news?hl=en"
        ]
    else:
        start_urls = [
        "https://news.google.co.kr/news/section?pz=1&cf=all&ned=us&topic=" + topic
        ]

    #now each 'title','image','desc' is printed in groups(clusters)
    #operation of dividing them into line by line in one cluster is needed''

    def parse(self, response):
        items = []
        for table in response.xpath('//table[@class="esc-layout-table"]'):
            item = GooglenewsenItem()
            item['title'] = table.xpath('.//div[@class="esc-lead-article-title-wrapper"]//span[@class="titletext"]/text()').extract()
            #if table.xpath('.//div[@class="esc-thumbnail-image-wrapper "]//img/@imgsrc').extract() is None:
            item['image'] = table.xpath('.//div[@class="esc-thumbnail-image-wrapper "]//img/@src').extract()
            #else:
            #   item['image'] = table.xpath('.//div[@class="esc-thumbnail-image-wrapper "]//img/@imgsrc').extract()
            item['desc'] = table.xpath('.//div[@class="esc-lead-snippet-wrapper"]/text()').extract()
            yield item
            items.append(item)

        section_name = response.xpath('.//div[@class="section-name"]/text()').extract()
    
        with open('googlenews_%s.txt' % section_name, 'a') as f:
            f.write('Current Topics are :')

            for topics in response.xpath('.//div[@class="topic"]'):
                topic = str(topics.xpath('.//a/text()').extract())
                #convert to string in order to avoid buffer problem
                f.write(topic)
            
            f.write('\n\n')

            for item in items:
                f.write('Title : {0}\nImage : {1}\nDesc : {2}\n\n'.format(item['title'], item['image'], item['desc']))


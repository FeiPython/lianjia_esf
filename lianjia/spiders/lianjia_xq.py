# -*- coding: utf-8 -*-
import scrapy
import datetime
from lianjia.items import LianjiaItem


class LianjiaXqSpider(scrapy.Spider):
    name = 'lianjia_xq'
    allowed_domains = ['lianjia.com']
    # start_urls = ['http://bj.lianjia.com/xiaoqu/?from=rec']
    start_urls = ['http://bj.lianjia.com/xiaoqu/1111027378112/']
    # start_urls = ['https://bj.lianjia.com/xiaoqu/pg5/']
    # start_urls = ['']

    # def start_requests(self):
    #     self.lists = []
    #     for i in range(1, 2):
    #         yield scrapy.Request(url='https://bj.lianjia.com/xiaoqu/pg%s/' % i,
    #                              callback=self.parse, dont_filter=True)

    def parse(self, response):

        # num = len(response.xpath('//ul[@class="listContent"]/li').extract())
        # print(num)
        with open('1.txt','w') as f:
            f.write(response.text)
        # f = open('5.txt', 'a')
        # lists = response.xpath('/html/body/div[1]/div[1]/text()').extract_first()
        # lists = response.xpath('//li[@class="pictext"]')
        # print(len(lists))
        # print('********************')
        # print(len(lists))
        # print('********************')
        # if lists:
        #     for data in lists:
        #         title = data.xpath('./a/div[2]/div[1]/text()')
        #         # f.write(title)
        #         if title not in self.lists:
        #             self.lists.append(title)
        #             print(title)
        # print(len(self.lists))
        # for data in lists:
        # f.close()
            # print(data.xpath('./div[1]/div[3]/a[1]/text()').extract_first())
            # print(response.urljoin(data.xpath('./div[1]/div[1]/a/text()').extract_first()))
            # print(response.urljoin(data.xpath('./div[1]/div[1]/a/@href').extract_first()))
            # print(data.xpath('./div[2]/div[1]/div[1]/span/text()').extract_first())
            # print(data.xpath('./div[2]/div[2]/a/span/text()').extract_first())
            # print(data.xpath('./div[1]/div[2]/a[1]/text()').extract_first())
        # for data in lists:
        #     item = LianjiaItem()
        #     item['areas'] = data.xpath('./div[1]/div[3]/a[1]/text()').extract_first()
        #     item['address'] = response.urljoin(data.xpath('./div[1]/div[1]/a/text()').extract_first())
        #     item['address_url'] = response.urljoin(data.xpath('./div[1]/div[1]/a/@href').extract_first())
        #     item['avg_price'] = data.xpath('./div[2]/div[1]/div[1]/span/text()').extract_first()
        #     item['num_listings'] = data.xpath('./div[2]/div[2]/a/span/text()').extract_first()
        #     panduan = data.xpath('./div[1]/div[2]/a[1]/text()').extract_first()
        #     if '户型' in panduan:
        #         item['num_moufinish'] = data.xpath('./div[1]/div[2]/a[2]/text()').extract_first()
        #         item['num_rents'] = data.xpath('./div[1]/div[2]/a[3]/text()').extract_first()
        #     else:
        #         item['num_moufinish'] = panduan
        #         item['num_rents'] = data.xpath('./div[1]/div[2]/a[2]/text()').extract_first()

            # yield scrapy.Request(item['address_url'], callback=self.parse_detail, meta=item)

        # url = response.xpath('//*[@id="main"]/div[7]/div/a[@rel="nofollow"]/@href').extract_first()
        # if url:
        #     url = response.urljoin(url)
        #     yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        item_dict = response.meta
        item = LianjiaItem()
        item['province'] = '北京'
        item['city'] = '北京市'
        item['areas'] = item_dict['areas']
        item['address'] = item_dict['address']
        item['avg_price'] = item_dict['avg_price']
        item['num_moufinish'] = item_dict['num_moufinish']
        item['num_listings'] = item_dict['num_listings']
        item['num_rents'] = item_dict['num_rents']
        item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
        item['num_buildings'] = response.xpath('/html/body/div[6]/div[2]/div[2]/div[6]/span[2]/text()').extract_first()
        item['num_houses'] = response.xpath('/html/body/div[6]/div[2]/div[2]/div[7]/span[2]/text()').extract_first()
        item['build_type'] = response.xpath('/html/body/div[6]/div[2]/div[2]/div[2]/span[2]/text()').extract_first()
        item['build_time'] = response.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/span[2]/text()').extract_first()
        item['developers'] = response.xpath('/html/body/div[6]/div[2]/div[2]/div[5]/span[2]/text()').extract_first()

        yield item

        pass

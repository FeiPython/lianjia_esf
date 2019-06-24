# -*- coding: utf-8 -*-
import scrapy
import time, re
from lianjia.items import LianjiaItem

class LianjiaZfSpider(scrapy.Spider):
    name = 'lianjia_esf'
    allowed_domains = ['lianjia.com']
    # start_urls = ['https://bj.lianjia.com/ershoufang/shunyi/pg1y4/']
    start_urls = ['']

    def start_requests(self):
        for i in range(1, 67):
            # url = 'https://m.lianjia.com/bj/ershoufang/shunyi/pg%sy4/' % i   # 顺义二手房20年以内
            # url = 'https://m.lianjia.com/bj/ershoufang/shunyi/pg%sy5/' % i   # 顺义二手房20年以上
            url = 'https://m.lianjia.com/bj/ershoufang/changping/pg%sy4lc2/' % i   # 昌平二手房20年以内
            # url = 'https://m.lianjia.com/bj/ershoufang/shunyi/pg%sy5/' % i   # 昌平二手房20年以上
            # time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        item = LianjiaItem()
        data_list = response.xpath('//body/div/div/section[1]/div[2]/div/div[4]/ul/li')
        first = response.xpath('//body/div/div/section[1]/div[2]/div/div[4]/ul/li[1]/span/text()')
        if first:
            for data in data_list:
                title = data.xpath('./div/div[2]/div[1]/text()').extract_first()
                if title:
                    url = data.xpath('./a/@href').extract_first()
                    prices = data.xpath('./div/div[2]/div[3]/span[1]/em/text()').extract_first()
                    price = data.xpath('./div/div[2]/div[3]/span[2]/text()').extract_first()
                    # print(url, title)
                    item['title'] = title if title else 'None'
                    item['prices'] = prices if prices else 'None'
                    item['price'] = price if price else 'None'
                    time.sleep(0.05)
                    # print(url)
                    yield scrapy.Request(url, callback=self.parse_detail, meta=item)

                    # break

    def parse_detail(self, response):
        item_dict = response.meta
        item = LianjiaItem()
        item['province'] = '北京'
        item['city'] = '北京市'
        item['areas'] = '顺义区'
        item['coordinate_type'] = '百度'
        item['crawl_time'] = '2019-5-30'
        item['title'] = item_dict['title']
        item['prices'] = item_dict['prices']
        item['price'] = item_dict['price']
        hou = response.xpath('//h3[@class="similar_data"]/div/div[2]/p[2]/text()').extract_first() # 3室2厅
        # if hou:
        area = response.xpath('//h3[@class="similar_data"]/div/div[3]/p[2]/text()').extract_first()
        address = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[12]/a/text()').extract_first()
        listing_time = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[2]/text()').extract_first()
        orient = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[3]/text()').extract_first()
        flo = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[4]/text()').extract_first()  # 底层/4
        fitment = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[7]/text()').extract_first()
        elevator = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[6]/text()').extract_first()
        build_type = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[5]/text()').extract_first()
        build_time = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[8]/text()').extract_first()
        quanshu = response.xpath('//ul[@class="house_description big lightblack lazyload_ulog"]/li[10]/text()').extract_first()
        # coordinate = response.xpath('//body/div[7]/div/a/@href').extract_first()
        coo = response.xpath('//div[@class="sub_mod_box location"]/div/a/@href').extract_first()

        item['hou'] = hou if hou else 'None'
        item['area'] = area if area else 'None'
        item['address'] = address if address else 'None'
        item['listing_time'] = listing_time if listing_time else 'None'
        item['orient'] = orient if orient else 'None'
        item['flo'] = flo if flo else 'None'
        item['fitment'] = fitment if fitment else 'None'
        item['elevator'] = elevator if elevator else 'None'
        item['build_type'] = build_type if build_type else 'None'
        item['build_time'] = build_time if build_time else 'None'
        item['quanshu'] = quanshu if quanshu else 'None'
        if coo:
            coordinate = re.search('pos=(\d+.\d+,\d+.\d+)', coo)
            item['coordinate'] = coordinate.group(1) if coordinate else 'None'
        else:
            item['coordinate'] = ''
        time.sleep(0.05)
        yield item
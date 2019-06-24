# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def __init__(self):
        self.file = open('3.txt', 'w')

    def process_item(self, item, spider):
        dict_data = dict(item)
        # dict_data['title'] = dict_data['title'].strip()
        # dict_data['release_time'] = dict_data['release_time'].split('：')[1]
        # dict_data['like'] = dict_data['like'].strip()

        # self.file.write(str_data)
        self.file.write(dict_data['province'] + ';' + dict_data['city'] + ';' + dict_data['areas'] + ';' +
                        dict_data['title'] + ';' + dict_data['listing_time'] + ';' + dict_data['prices'] + ';' +
                        dict_data['price'] + ';' + dict_data['hou'] + ';' + dict_data['area'] + ';' +
                        dict_data['orient'] + ';' + dict_data['flo'] + ';' + dict_data['fitment'] + ';' +
                        dict_data['elevator'] + ';' + dict_data['address'] + ';' + dict_data['coordinate'] + ';' +
                        dict_data['coordinate_type'] + ';' + dict_data['build_type'] + ';' + dict_data['build_time'] + ';' +
                        dict_data['crawl_time'] + ';' + dict_data['quanshu'] + '\n')

        return item

    def __del__(self):
        self.file.close()

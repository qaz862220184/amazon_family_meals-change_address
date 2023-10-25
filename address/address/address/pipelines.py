# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from common.core.mongodb.mongo import MongoDb


class AddressPipeline:
    def process_item(self, item, spider):
        MongoDb.table('address_cookie_pool').insert_one(dict(item))
        return item

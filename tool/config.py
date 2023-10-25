# -*- coding: UTF-8 -*-
from common.utils.cache import Chcaed
from common.core.mongodb.mongo import MongoDb
from datetime import datetime
from bson.objectid import ObjectId


class Config(object):

    @classmethod
    def get_country(cls, key=None):
        """
        获取国家数据
        :param key:
        :return:
        """
        data_key = 'country_data_key'
        country = Chcaed.get(data_key)
        if country is None:
            country = {}
            result = MongoDb.table('scrapy_country').find({'status': {'$eq': 1}})
            if result:
                for item in result:
                    for filed in item:
                        if isinstance(item[filed], datetime) or isinstance(item[filed], ObjectId):
                            item[filed] = str(item[filed])
                    country[item['code']] = item
            if country:
                Chcaed.put(data_key, country, 3600)
        if key is not None and country:
            return country[key]
        return country


if __name__ == '__main__':
    Config.get_country('US')

# -*- coding: UTF-8 -*-
import json
import requests
import time
from common.core.mongodb.mongo import MongoDb
from common.settings import SITE_ADDRESS_POOL


def pool_view():
    crawl_url = 'http://localhost:6800/schedule.json?project=address&spider=patrol'
    pool_info = get_pool_info()
    for country in SITE_ADDRESS_POOL:
        value = SITE_ADDRESS_POOL.get(country)
        pool_size = value.get('pool_size')
        if not pool_info.get(country) or pool_size > pool_info.get(country):
            # 使用接口去调用爬虫
            params = {'country_code': country, 'zip_code': value.get('zip_code')}
            params = json.dumps(params)
            requests.post(crawl_url, params={'params': params})


def get_pool_info():
    # 查找每个国家的cookie数量
    pool_dict = {}
    pool_info = MongoDb.table('address_cookie_pool').get_collection().aggregate(
        [
            {
                '$group': {
                    '_id': '$country_code',
                    'count': {'$sum': 1}
                }
            }
        ]
    )
    for info in pool_info:
        pool_dict[info['_id']] = info['count']
    return pool_dict


if __name__ == '__main__':
    while True:
        try:
            pool_view()
        except:
            time.sleep(1)

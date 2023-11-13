# -*- coding: UTF-8 -*-
import requests
import json
from common.core.mongodb.mongo import MongoDb
from common.settings import SITE_ADDRESS_POOL


def apply_cookie(params):
    url = 'http://localhost:6800/schedule.json?project=address&spider=patrol'
    new_url = url + '&params=' + json.dumps(params)
    response = requests.post(new_url)
    print(response.text)


if __name__ == '__main__':
    for key in SITE_ADDRESS_POOL:
        result = MongoDb.table('address_cookie_pool').get_collection().count_documents({'country_code': key})
        pool_size = SITE_ADDRESS_POOL[key].get('pool_size')
        if result < pool_size:
            params = {'country_code': key, 'zip_code': SITE_ADDRESS_POOL[key].get('zip_code')}
            apply_cookie(params)

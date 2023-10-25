import scrapy
import json
import sys
sys.path.append("..")
sys.path.append("../..")
from tool.request.cookies.change_address import AmazonLocationSession
from ..items import AddressItem


class PatrolSpider(scrapy.Spider):
    name = "patrol"
    proxy = 'http://127.0.0.1:3213'
    start_urls = ['http://localhost:6800/jobs']

    def __init__(self, params=None, *args, **kwargs):
        super().__init__(params)
        if not params:
            raise ValueError('参数不存在')
        params = json.loads(params)
        self.country_code = params.get('country_code')
        self.zip_code = params.get('zip_code')

    def parse(self, response, **kwargs):
        """
        定时维护cookie池
        :return:
        """
        amazon = AmazonLocationSession(self.country_code, self.zip_code, {'https': self.proxy})
        cookies = amazon.change_address()
        if not cookies:
            raise ValueError('cookie is not acquire')

        item = AddressItem()
        item["country_code"] = self.country_code
        item["zip_code"] = self.zip_code
        item["cookies"] = json.dumps(cookies)
        yield item

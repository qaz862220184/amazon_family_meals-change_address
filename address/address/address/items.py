# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AddressItem(scrapy.Item):
    # define the fields for your item here like:
    country_code = scrapy.Field()
    zip_code = scrapy.Field()
    cookies = scrapy.Field()


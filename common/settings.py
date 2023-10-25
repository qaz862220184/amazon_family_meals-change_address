import pymysql
# from urllib import parse

# mysqldb
DB_MYSQL_CONF = {
    "host": "127.0.0.1",
    "user": "inventory",
    "passwd": "hwFccnZDRWzJtd75",
    "db": "inventory",
    "charset": "utf8",
    "port": 3306,
    "prefix": 'is_',
    "cursorclass": pymysql.cursors.DictCursor,
}

# mongodbpython
DB_MONGODB_CONF = {
    "default": {
            "uri": "mongodb://127.0.0.1:27017",
            "database": "common_service",
            "prefix": 'xx_',
        }
}

# redisdb
DB_REDIS_CONF = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 0,
    "max_connections": 10,
    "connection_kwargs": {
        "decode_responses": True,
    },
}

# cache
CACHE_CONF = {
    "driver": 'redis',
    "prefix": 'amazon_scrapy_cache',
}

# 每个站点的池子配置信息
SITE_ADDRESS_POOL = {
    'US': {
        'country_code': 'US',
        'domain': 'www.amazon.com',
        'language': 'en-US',
        'zip_code': '90001',
        'pool_size': 100
    },
    'GB': {
        'country_code': 'GB',
        'domain': 'www.amazon.co.uk',
        'language': '',
        'zip_code': 'M25BQ',
        'pool_size': 100
    },
    'CA': {
        'country_code': 'CA',
        'domain': 'www.amazon.ca',
        'language': 'en_CA',
        'zip_code': 'M5S 2E8',
        'pool_size': 100
    },
    'JP': {
        'country_code': 'JP',
        'domain': 'www.amazon.co.jp',
        'language': 'ja_JP',
        'zip_code': '100-8050',
        'pool_size': 100
    },
    'FR': {
        'country_code': 'FR',
        'domain': 'www.amazon.fr',
        'language': '',
        'zip_code': '75000',
        'pool_size': 100
    },
    'DE': {
        'country_code': 'DE',
        'domain': 'www.amazon.de',
        'language': 'de_DE',
        'zip_code': '01169',
        'pool_size': 100
    },
    'ES': {
        'country_code': 'ES',
        'domain': 'www.amazon.es',
        'language': 'es_ES',
        'zip_code': '08007',
        'pool_size': 100
    },
    'IT': {
        'country_code': 'IT',
        'domain': 'www.amazon.it',
        'language': '',
        'zip_code': '30126',
        'pool_size': 100
    },
    'PL': {
        'country_code': 'PL',
        'domain': 'www.amazon.pl',
        'language': '',
        'zip_code': '00-005',
        'pool_size': 100
    },
    'SE': {
        'country_code': 'SE',
        'domain': 'www.amazon.se',
        'language': 'sv_SE',
        'zip_code': '100 12',
        'pool_size': 100
    },
    'SG': {
        'country_code': 'SG',
        'domain': 'www.amazon.sg',
        'language': '',
        'zip_code': '670102',
        'pool_size': 100
    },
    'MX': {
        'country_code': 'MX',
        'domain': 'www.amazon.com.mx',
        'language': '',
        'zip_code': '11529',
        'pool_size': 100
    },
    'IN': {
        'country_code': 'IN',
        'domain': 'www.amazon.in',
        'language': '',
        'zip_code': '141001',
        'pool_size': 100
    },
    'BR': {
        'country_code': 'BR',
        'domain': 'www.amazon.com.br',
        'language': '',
        'zip_code': '59510-000',
        'pool_size': 100
    },
    'NL': {
        'country_code': 'NL',
        'domain': 'www.amazon.nl',
        'language': '',
        'zip_code': 'NL',
        'pool_size': 100
    },
    'AU': {
        'country_code': 'AU',
        'domain': 'www.amazon.com.au',
        'language': '',
        'zip_code': '3175',
        'pool_size': 100
    },
    'AE': {
        'country_code': 'AE',
        'domain': 'www.amazon.ae',
        'language': '',
        'zip_code': 'Al Ain',
        'pool_size': 100
    },
    'SA': {
        'country_code': 'SA',
        'domain': 'www.amazon.sa',
        'language': 'ar_AE',
        'zip_code': 'Riyadh',
        'pool_size': 100
    },
    'EG': {
        'country_code': 'EG',
        'domain': 'www.amazon.eg',
        'language': 'ar_AE',
        'zip_code': 'Mansoura',
        'pool_size': 100
    },
    'TR': {
        'country_code': 'TR',
        'domain': 'www.amazon.com.tr',
        'language': '',
        'zip_code': '',
        'pool_size': 100
    },
}

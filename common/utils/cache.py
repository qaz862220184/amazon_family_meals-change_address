# -*- coding: UTF-8 -*-
import json
from common.settings import CACHE_CONF
from common.core.redisdb.redis_pool import RedisClient
from common.utils.encryption import Md5Encrytion


class Chcaed(object):
    driver = CACHE_CONF['driver']
    prefix = CACHE_CONF['prefix']

    @classmethod
    def put(cls, key, value, ex=0):
        """
        缓存写入
        :param key:
        :param value:
        :param ex:
        :return:
        """
        if ex > 0:
            return cls.get_driver().set(cls.get_cache_key(key), json.dumps(value), ex)
        else:
            return cls.get_driver().set(cls.get_cache_key(key), json.dumps(value))

    @classmethod
    def get(cls, key):
        """
        读取缓存
        :param key:
        :return:
        """
        res = cls.get_driver().get(cls.get_cache_key(key))
        if res:
            return json.loads(res)
        return None

    @classmethod
    def delete(cls, key):
        """
        删除缓存
        :param key:
        :return:
        """
        return cls.get_driver().delete(cls.get_cache_key(key))

    @classmethod
    def clear(cls):
        """
        清除所有缓存
        :return:
        """
        keys = cls.get_driver().keys(cls.prefix + '*')
        return cls.get_driver().delete(*keys)

    @classmethod
    def get_cache_key(cls, key):
        """
        获取缓存key
        :param key:
        :return:
        """
        if isinstance(key, str) is False and isinstance(key, bytes) is False:
            key = cls.create_key_by_params(key)
        return '_'.join([cls.prefix, key])

    @classmethod
    def get_driver(cls):
        """
        获取缓存扩展
        :return:
        """
        if cls.driver == 'redis':
            return RedisClient.redis()

    @classmethod
    def create_key_by_params(cls, params, pre=''):
        """
        根据参数生成一个缓存key
        :param params:
        :param pre:
        :return:
        """
        params_json = json.dumps(params)
        return pre + Md5Encrytion.md5_lower32(params_json)

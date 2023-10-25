# -*- coding: UTF-8 -*-
from urllib.parse import urlparse
from common.helpers import get_value
import mimetypes
import os


class UrlParse:
    """
    url解析
    """

    def __init__(self, url):
        self.url = url
        self.parsed_obj = urlparse(url)
        # 来着query中的参数
        self.param = {}

    def get_scheme(self):
        """
        获取协议
        :return:
        """
        scheme = self.parsed_obj.scheme
        if not scheme:
            scheme = 'http'
        return scheme

    def get_domain(self):
        """
        获取域名
        :return:
        """
        return self.parsed_obj.netloc

    def get_port(self):
        """
        获取端口号
        :return:
        """
        domain = self.get_domain()
        arr = domain.split(':')
        if len(arr) == 2:
            return arr[1]
        else:
            return 80

    def get_path(self):
        """
        获取url路径
        :return:
        """
        path = self.parsed_obj.path
        if not path:
            path = '/'
        return path

    def get_query(self):
        """
        获取查询参数
        """
        return self.parsed_obj.query

    def get_referer(self):
        """
        获取来源
        :return:
        """
        return f"{self.get_scheme()}://{self.get_domain()}"

    def get_param_by_query(self, name=None, default=None):
        """
        获取来自query的请求参数
        :param name:
        :param default:
        :return:
        """
        if not self.param:
            query = self.get_query()
            for key_val in query.split('&'):
                if not key_val:
                    continue
                tup = tuple(str(key_val).split('='))
                if len(tup) == 2:
                    key, val = tup
                    self.param[key] = val

        return get_value(
            result=self.param,
            name=name,
            default=default
        )


class File:

    def __init__(self, filename):
        self.filename = filename
        # 验证
        self.__check()
        self.__stat = os.stat(self.filename)
        self.__base_name = None
        self.__mime = None

    def create_upload_file(self, form_name='file', new_filename=None):
        """
        创建上传的文件
        :param form_name:
        :param new_filename:
        :return:
        """
        if not new_filename:
            new_filename = self.get_base_name()
        fileinfo = (new_filename, open(self.filename, 'rb'), self.get_mime_types())
        return form_name, fileinfo

    def get_base_name(self):
        """
        获取文件名称
        :return:
        """
        if not self.__base_name:
            self.__base_name = os.path.basename(self.filename)
        return self.__base_name

    def get_ext(self):
        """
        获取扩展名
        :return:
        """
        base_name = self.get_base_name()
        arr = base_name.split('.')
        return arr[1] if len(arr) == 2 else None

    def get_mime_types(self):
        """
        获取文件类型
        :return:
        """
        if not self.__mime:
            self.__mime = mimetypes.guess_type(self.filename)
        return self.__mime[0] if len(self.__mime) >= 1 else None

    def get_mode(self):
        """
        获取权限
        :return:
        """
        return self.__get_stat(
            name='st_mode'
        )

    def get_size(self):
        """
        获取文件大小
        :return:
        """
        return self.__get_stat(
            name='st_size'
        )

    def get_atime(self):
        """
        获取最后活动时间
        :return:
        """
        return self.__get_stat(
            name='st_atime'
        )

    def get_mtime(self):
        """
        获取最后编辑时间
        :return:
        """
        return self.__get_stat(
            name='st_mtime'
        )

    def get_ctime(self):
        """
        获取创建时间
        :return:
        """
        return self.__get_stat(
            name='st_ctime'
        )

    def __get_stat(self, name=None):
        """
        获取文件统计信息
        :param name:
        :return:
        """
        return getattr(self.__stat, name)

    def __check(self):
        """
        检查文件
        :return:
        """
        if os.path.isfile(self.filename) is False:
            raise ValueError('File does not exist:' + self.filename)

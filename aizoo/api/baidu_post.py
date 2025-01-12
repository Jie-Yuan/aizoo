#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'kg'
__author__ = 'JieYuan'
__mtime__ = '19-3-25'
"""

import json
import urllib

import requests
from meutils.pipe import *


class BaiduPost(object):
    """
    知识图谱： https://aip.baidubce.com/rpc/2.0/kg/v1/cognitive/entity_annotation
    智能春联： https://aip.baidubce.com/rpc/2.0/nlp/v1/couplets
        { "text": "百度", "index": 0}
    智能写诗: https://aip.baidubce.com/rpc/2.0/nlp/v1/poem
        { "text": "百度", "index": 0} # index默认为数值为0，即第一首诗。每换一次，数值加1即可，一定数量后会返回之前的作诗结果

    """

    def __init__(self, api_key='20190718000319131', secret_key='goP6CsXs6sVamHtRGdBa'):
        self.access_token = self._get_access_token(api_key, secret_key)

    def predict(self, input_text, url):
        url = url + '?charset=UTF-8&access_token=' + self.access_token

        # the input is json format
        # input_text = {'data': text}
        r = requests.post(url, json=input_text)
        return r.json()

    def _get_access_token(self, api_key, secret_key):

        url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}'

        _ = requests.get(url).json()

        print(_)

        return _['access_token']


if __name__ == '__main__':
    from pprint import pprint

    api = BaiduPost()
    pprint(api.predict({'data': '周杰伦'},
                       'https://aip.baidubce.com/rpc/2.0/kg/v1/cognitive/entity_annotation'))

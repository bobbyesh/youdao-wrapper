# api.py
'''Defines a YouDao class for accessing the public
youdao.com api.


Instantiating With API Key
==========================

>>> youdao = YouDao(keyfrom, key)


Instantiating With Config File
==============================

Create a keys.ini in the following format,
replace <keyfrom> and <key> with the keyfrom
and key that youdao provided:

# keys.ini
[DEFAULT]
keyfrom = <keyfrom>
key = <key>

>>> youdao = YouDao.from_config('keys.ini')


Making Queries
==============

The `get` method returns a dictionary with the
word, its definitions, and the pinyin.

After instantiating with one of the above methods:

>>> query = youdao.get('你好')
>>> query
{'word': '你好', 'pinyin': 'nǐ hǎo', 'def': ['hello；hi']}

'''



from urllib.parse import quote
import requests
import configparser


class YouDao(object):
    '''

    ..TODO:  Detect when the translation doesn't actually exist.

    '''

    error_messages = {
        0: 'Normal',
        20: 'The request string was too long',
        30: 'Unable to efficiently translate',
        40: 'Unsupported language type',
        50: 'Invalid key',
        60: 'No dictionary results',
    }

    def __init__(self, keyfrom, key):
        self.keyfrom = keyfrom
        self. key = key
        self.response = None

    @classmethod
    def from_config(cls, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        keyfrom = config['DEFAULT']['keyfrom']
        key = config['DEFAULT']['key']
        return cls(keyfrom, key)


    def get(self, query):
        '''Returns a dictionary with the word, definitions, and pinyin.'''
        json = self.get_json(query)
        definitions = json['basic']['explains']
        pinyin = json['basic']['phonetic']
        word = json['query']
        return {'def': definitions,
                'pinyin': pinyin,
                'word': word}

    def get_json(self, query):
        url = self.url(query)
        self.response= requests.get(url)
        return self.response.json()

    def get_jsonp(self, query):
        url = self.url(query, doctype='jsonp')
        self.response= requests.get(url)
        return response.json()

    def json(self):
        if not self.response:
            raise Exception('No response object yet, must call get() first.')
        return self.response.json()

    def url(self, query, doctype='json'):
        return ('http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s'
                '&type=data&doctype=%s&version=1.1&q=') % (self.keyfrom, self.key, doctype) + quote(query)

    def handle_error(self, json):
        code = json['error_code']
        if code != 0:
            raise Exception( self.error_messages[code] )





def test_url():
    with open('keys', 'r') as f:
        key = f.readline().strip()
        keyfrom = f.readline().strip()

    return URL(keyfrom, key, '悲壮')




if __name__ == '__main__':
    import os
    import json
    key = None
    keyfrom = None

    config = configparser.ConfigParser()
    config.read('keys.ini')
    print(config['DEFAULT']['key'])
    print(config['DEFAULT']['keyfrom'])


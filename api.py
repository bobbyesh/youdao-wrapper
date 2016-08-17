# api.py

from urllib.parse import quote
import requests


class YouDao(object):

    def __init__(self, keyfrom, key):
        self.keyfrom = keyfrom
        self. key = key
        self.response = None

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
        return response.json()

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



def test_url():
    with open('keys', 'r') as f:
        key = f.readline().strip()
        keyfrom = f.readline().strip()

    return URL(keyfrom, key, '悲壮')




if __name__ == '__main__':
    import os
    key = None
    keyfrom = None
    with open('keys', 'r') as f:
        key = f.readline().strip()
        keyfrom = f.readline().strip()

    youdao = YouDao(keyfrom, key)
    query = '悲壮'

    json = youdao.get_json(query)
    print(json)

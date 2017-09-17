#!/usr/bin/env python
# coding=utf8

import requests
from bs4 import BeautifulSoup
import json
import random

class KuaiDi():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Host': 'www.kuaidi100.com',
            'Referer': 'https://www.kuaidi100.com/'
        }
        self.main_url = 'www.kuaidi100.com'


    def query(self, ticket):
        type = self.auto_query_type(ticket)
        if type is None:
            print('get tyep error')
        if self.query_delivery_progress(type, ticket) is None:
            print('get progress error')


    def auto_query_type(self, ticket):
        url = 'https://www.kuaidi100.com/autonumber/autoComNum'
        payload = { 'text': ticket}
        html = requests.get(url, headers=self.headers, params=payload)
        if html.status_code != requests.codes.ok:
            return None
        result = json.loads(html.text)
        company_code = result['auto'][0]['comCode']
        return company_code


    def query_delivery_progress(self, type, ticket):
        url = 'https://www.kuaidi100.com/query'
        payload = { 
            'type': type,
            'postid': ticket,
            'id': 1,
            'valicode': '',
            'temp': random.random() 
        }
        html = requests.get(url, headers=self.headers, params=payload)
        if html.status_code != requests.codes.ok:
            return None
        result = json.loads(html.text)
        for data in result['data']:
            print(data['time'],data['context'])
        return result['data']

if __name__ == '__main__':
    kuaidi = KuaiDi()
    kuaidi.query('667639515710')
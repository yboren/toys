#!/usr/bin/env python
# coding=utf8

import requests
from bs4 import BeautifulSoup
import json
import random
import xml.etree.ElementTree as ET

class Weather():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Host': 'www.weather.com.cn',
        }
        self.citylist_url = 'http://mobile.weather.com.cn/js/citylist.xml'
        self.realtime_template_url = 'http://www.weather.com.cn/data/sk'
        self.next_template_url = 'http://mobile.weather.com.cn/data/forecast'


    def query(self, city):
        city_code = self.get_code(city)
        if city_code is None:
            return False
        #realtime weather
        url = '%s/%s.html' % (self.realtime_template_url, city_code)
        print(url)
        html = requests.get(url, headers=self.headers)
        if html.status_code != requests.codes.ok:
            return None
        result = json.loads(html.text.encode('latin-1').decode('utf8'))
        print(result['weatherinfo'])
        return result
        #next 6 days weather
        url = '%s/%s.html' % (self.next_template_url, city_code)
        print(url)
        html = requests.get(url, headers=self.headers)
        if html.status_code != requests.codes.ok:
            return None
        result = json.loads(html.text)
        print(result)
        return result


    def get_code(self, city):
        tree = ET.ElementTree(file='citylist.xml')
        for elem in tree.iter(tag='d'):
            if(elem.attrib['d2'] == city):
                print(city, elem.attrib['d1'])
                return elem.attrib['d1']
        return None

if __name__ == '__main__':
    weather = Weather()
    weather.query('西安')
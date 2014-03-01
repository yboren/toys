#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import json
import sys


def ip_query(ip):
    ip_url = 'http://ip.taobao.com/service/getIpInfo.php'  # ip=x.x.x.x
    payload = {'ip': ip}
    result_json = requests.get(ip_url, params=payload)
    if result_json.status_code != 200:
        return False
    result = json.loads(result_json.content)
    if result['code'] == 0:
        return result['data']['country'] + \
            result['data']['area'] + result['data']['region']
    else:
        return False


if __name__ == "__main__":
    location = ip_query(sys.argv[1])
    if location:
        print location
    else:
        print "query fail!"

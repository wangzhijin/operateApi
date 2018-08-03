"""This is a test program."""
# -*- coding: utf-8 -*-

import json
import requests
import time
import hashlib
import json as complex_json

# jsonファイルからapiキー・アクセスキーを取得
COINCHECK_KEYS_JSON = open('coinex_keys.json', 'r')
# jsonパース
COINCHECK_KEYS = json.load(COINCHECK_KEYS_JSON)

class CoinEx:
    """
    参考ページ
    https://github.com/coinexcom/coinex_exchange_api/wiki
    """
    __headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    }

    def __init__(self):
        self.access_id = COINCHECK_KEYS["accessid"]
        self.secret_key = COINCHECK_KEYS["secretkey"]
        self.headers = self.__headers
        self.url = 'https://api.coinex.com/v1'

    @staticmethod
    def get_sign(params, secret_key):
        sort_params = sorted(params)
        data = []
        for item in sort_params:
            data.append(item + '=' + str(params[item]))
        str_params = "{0}&secret_key={1}".format('&'.join(data), secret_key)
        token = hashlib.md5(str_params.encode('utf-8')).hexdigest().upper()
        return token

    def set_authorization(self, params):
        params['access_id'] = self.access_id
        params['tonce'] = int(time.time()*1000)
        self.headers['AUTHORIZATION'] = self.get_sign(params, self.secret_key)

    def request(self, method, url, params={}, data='', json={}):
        method = method.upper()
        if method in ['GET', 'DELETE']:
            self.set_authorization(params)
            result = requests.get(method, url, fields=params, headers=self.headers)
        else:
            if data:
                json.update(complex_json.loads(data))
            self.set_authorization(json)
            encoded_data = complex_json.dumps(json).encode('utf-8')
            result = requests.post(method, url, body=encoded_data, headers=self.headers)
        return result

    def ticker(self):
        """ ティッカー [GET] """

        print("\nティッカー [GET]")
        url = 'https://api.coinex.com/v1/market/ticker/all'
        coinex = requests.get(url).json()
        for key in coinex.keys():
            print(key, ":")
            print(coinex[key])

    def getAccountInfo(self):
        self.set_authorization({})
        url = 'https://api.coinex.com/v1/balance/info'
        params = {}
        params['access_id'] = self.access_id
        params['tonce'] = int(time.time()*1000)
        result = requests.get(url, params=params,headers=self.headers).json()
        for key in result.keys():
            print(key, ":")
            if key == "data":
                for key2 in result[key].keys():
                    tmpStr = ""
                    for value,item in result[key][key2].items():
                        if float(item) > 0:
                            tmpStr = tmpStr + " " + value + ":" + item
                    if tmpStr != "":
                        print(key2, tmpStr)
            else:
                print(result[key])

if __name__ == '__main__':
    CE = CoinEx()
    CE.ticker()
    CE.getAccountInfo()


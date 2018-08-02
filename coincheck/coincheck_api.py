"""coincheck private api execute program."""
# -*- coding: utf-8 -*-

import json
import requests
import time
import hmac
import hashlib

# jsonファイルからapiキー・アクセスキーを取得
COINCHECK_KEYS_JSON = open('coincheck_keys.json', 'r')
# jsonパース
COINCHECK_KEYS = json.load(COINCHECK_KEYS_JSON)

# 新規注文 [POST]
PATH_ORDERS = '/api/exchange/orders'
# 未決済の注文一覧[GET]
PATH_ORDERS_OPENS = '/api/exchange/orders/opens'
# 注文のキャンセル [DELETE] 末尾に+id(キャンセルしたい新規注文または未決済の注文一覧のID)
PATH_ORDERS_CANCEL = '/api/exchange/orders/'

class CoinCheck:
    """ definition get/post/delete method. """
    def __init__(self):
        self.access_key = COINCHECK_KEYS["accesskey"]
        self.secret_key = COINCHECK_KEYS["secretkey"]
        self.url = 'https://coincheck.com'

    def get(self, path, params=None):
        """ get method. """
        if params != None:
            params = json.dumps(params)
        else:
            params = ''
        nonce = str(int(time.time()))
        message = nonce + self.url + path + params
        signature = self.get_signature(message)

        return requests.get(
            self.url + path,
            headers=self.get_header(self.access_key, nonce, signature)
        ).json()

    def post(self, path, params):
        """ post method. """
        params = json.dumps(params)
        nonce = str(int(time.time()))
        message = nonce + self.url + path + params
        signature = self.get_signature(message)

        return requests.post(
            self.url + path,
            data=params,
            headers=self.get_header(self.access_key, nonce, signature)
        ).json()

    def delete(self, path):
        """ delete method. """
        nonce = str(int(time.time()))
        message = nonce + self.url + path
        signature = self.get_signature(message)

        return requests.delete(
            self.url + path,
            headers=self.get_header(self.access_key, nonce, signature)
        ).json()

    def get_signature(self, message):
        """ get signature. """
        signature = hmac.new(
            bytes(self.secret_key.encode('ascii')),
            bytes(message.encode('ascii')),
            hashlib.sha256
        ).hexdigest()

        return signature

    def get_header(self, access_key, nonce, signature):
        """ get header. """
        headers = {
            'ACCESS-KEY': access_key,
            'ACCESS-NONCE': nonce,
            'ACCESS-SIGNATURE': signature,
            'Content-Type': 'application/json'
        }

        return headers

    def buy(self, rate, amount):
        """ 指値注文 現物取引 買い """
        return self.order(rate, amount, 'buy')

    def leverage_buy(self, rate, amount):
        """ 指値注文のレバレッジ取引新規買い(rateがnullの場合、成行注文) """
        return self.order(rate, amount, 'leverage_buy')

    def order(self, rate, amount, order_type):
        """ 新規注文 [POST] """
        params = {
            "pair": "btc_jpy",
            "order_type": order_type,
            "rate": rate,
            "amount": amount,
        }
        return self.post(PATH_ORDERS, params)

    def orders_opens(self):
        """ 未決済の注文一覧[GET] """
        return self.get(PATH_ORDERS_OPENS)

    def orders_cancel(self, id):
        """ 注文のキャンセル [DELETE] """
        return self.delete(PATH_ORDERS_CANCEL + str(id))

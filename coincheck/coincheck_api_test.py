"""This is a test program."""
# -*- coding: utf-8 -*-

import requests

class CoinCheck:
    """
    参考ページ
    https://qiita.com/ti-ginkgo/items/7e15bdac6618c07534be
    """

    def ticker(self):
        """ ティッカー [GET] """

        print("\nティッカー [GET]")
        url = 'https://coincheck.com/api/ticker'
        coincheck = requests.get(url).json()
        for key, item in coincheck.items():
            print("%-9s : %-10.9s " % (key, item))

    def trades(self):
        """ 全取取引履歴 [GET] """

        print("\n全取取引履歴 [GET]")
        url = 'https://coincheck.com/api/trades'
        coincheck = requests.get(url, params={"pair": "btc_jpy"}).json()
        print(coincheck)

    def order_books(self):
        """ 板情報 [GET] """

        print("\n板情報 [GET]")
        url = 'https://coincheck.com/api/order_books'
        coincheck = requests.get(url).json()
        for key in coincheck.keys():
            print(key, ":")
            for value in coincheck[key]:
                print(value)
            print()

    def rate(self):
        """ レート [GET] """

        print("\nレート [GET]")
        url = 'https://coincheck.com/api/exchange/orders/rate'
        params = {'order_type': 'sell', 'pair': 'btc_jpy', 'amount': 0.1}
        coincheck = requests.get(url, params=params).json()
        print(coincheck)

        params = {'order_type': 'buy', 'pair': 'btc_jpy', 'price': 280000}
        coincheck = requests.get(url, params=params).json()
        print(coincheck)

    def sale_rate(self):
        """ 販売レート [GET] """

        print("\n販売レート [GET]")
        coins = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy',
                 'XEM': 'xem_jpy', 'BCH': 'bch_jpy'}

        url = 'https://coincheck.com/api/rate/'

        for key, item in coins.items():
            coincheck = requests.get(url+item).json()
            print("%-4s : %-10s" % (key, coincheck['rate']))

if __name__ == '__main__':
    CC = CoinCheck()
    CC.ticker()
    CC.trades()
    CC.order_books()
    CC.rate()
    CC.sale_rate()

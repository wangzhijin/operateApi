"""This is a test program."""
# -*- coding: utf-8 -*-

import requests

class CoinEx:
    """
    参考ページ
    https://github.com/coinexcom/coinex_exchange_api/wiki
    """

    def ticker(self):
        """ ティッカー [GET] """

        print("\nティッカー [GET]")
        url = 'https://api.coinex.com/v1/market/list'
        coinex = requests.get(url).json()
        for key in coinex.keys():
            print(key, ":")
            print(coinex[key])

if __name__ == '__main__':
    CE = CoinEx()
    CE.ticker()


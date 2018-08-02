""" 注文実行 """
# -*- coding: utf-8 -*-

import coincheck_api
import pandas as pd

if __name__ == '__main__':
    # create coincheck private api instance.
    CC = coincheck_api.CoinCheck()

    # 80万の指値で0.005ビットコインを買い注文
    # result = CC.buy(rate=800000, amount=0.005)
    # print(result)
    """
    {'order_type': 'buy', 'created_at': '2018-01-30T09:27:08.288Z', 'success': True, 'pair': 'btc_jpy', 'market_buy_amount': None, 'rate': '800000.0', 'id': 712953933, 'stop_loss_rate': None, 'amount': '0.005'}
    """

    # 未決済の注文一覧[GET]
    OPENS = CC.orders_opens()
    # print(OPENS)
    """
    {'orders': [{'order_type': 'buy', 'created_at': '2018-01-30T09:27:08.000Z', 'rate': '800000.0', 'id': 712953933, 'pending_market_buy_amount': None, 'stop_loss_rate': None, 'pair': 'btc_jpy', 'pending_amount': '0.005'}], 'success': True}
    """
    if OPENS['success']:
        print('success')
        df = pd.DataFrame(OPENS['orders'])
        pass

    # 注文のキャンセル [DELETE]
    # result = CC.orders_cancel(id)
    # print(result)

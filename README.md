# operateApi
# 各取引所のapi操作
[coincheck](https://coincheck.com/)  
[coinex](https://www.coinex.com/account/signin)

## 使い方
coincheckを例として説明させてください：
coincheck_keys.jsonというファイルを作成して、api操作用の鍵を記入してください。
```
// テンプレートファイルをコピー
cp coincheck_keys_tmp.json coincheck_keys.json
```

coincheck_api.pyをインポートして、CoinCheckインスタンスを生成して使用してください。
```
import coincheck_api

if __name__ == '__main__':
    # create coincheck private api instance.
    CC = coincheck_api.CoinCheck()

    # 80万の指値で0.005ビットコインを買い注文
    # result = CC.buy(rate=800000, amount=0.005)
    # print(result)
    """
    {'order_type': 'buy', 'created_at': '2018-01-30T09:27:08.288Z', 'success': True, 'pair': 'btc_jpy', 'market_buy_amount': None, 'rate': '800000.0', 'id': 712953933, 'stop_loss_rate': None, 'amount': '0.005'}
    """
```

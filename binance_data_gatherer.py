# -*- coding: utf-8 -*-
"""binance_data_gatherer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GxoBt4heSf_Iqmcinh5YA31Oaaxxetgo
"""

!pip install python-binance

from google.colab import drive
drive.mount('/content/drive/')

from binance.client import Client
from time import sleep
import pandas as pd
api_key = "w3u91JH32YEZGxAVWhKUSbUwXjEn3J2EyOq3ec31ArT1fsQfOZEsmAsuTRIIdq8p"
api_secret = "jpU7ObQfOxujNvq7YCtoWRROOKmuZFAeMh3n2MzlcUEEWGGaBvDTMaItP6fQhtmH"
client = Client(api_key, api_secret)

def get_minute_data(symbol, start_date, end_date, name = False):
    # NB: Alle inputs skal være strings.
    # dato-format skal være således: "1 Jan, 2018"
        
    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, start_date, end_date)
    df = pd.DataFrame(klines, columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ]) # tb -> Taker buy, av -> asset volume
    df = df.rename(columns={'open_time': 'time'})
    df.set_index('time', inplace=True)
    df = df[["close","volume"]]
    if not name:
        df.to_csv(f'/content/drive/My Drive/Machine Learning/crypto_data/{symbol}-1m-klines-{start_date}.csv')
    elif name:
        df.to_csv(f'/content/drive/My Drive/Machine Learning/crypto_data/{name}.csv')
    
    sleep(60)
    
    print(f"{symbol} 5M klines from {start_date} to {end_date} are saved!")

# Getting top coins from Binance
ratios_to_get = ["BTCUSDT", "XRPBTC", "XRPUSDT", "ETHUSDT", "ETHBTC", "EOSUSDT", "EOSBTC", "BCCUSDT", "BCCBTC", "LTCBTC", "LTCUSDT", "BNBUSDT", "BNBBTC"]
for ratio in ratios_to_get:
    get_minute_data(ratio, "1 Jun, 2018", "2 Oct, 2018", f"{ratio}-5M-Binance-2018")
import pandas as pd


def generate_bar(data):
    ## Data is a pandas dataframe
    open_price = data['open'][0]
    close = data['close'][len(data) - 1]
    high = data['high'].max()
    low = data['low'].min()
    volume_ave = data['volume'].mean()
    OHLC = pd.DataFrame(data = [[close, high, low, open_price, volume_ave]], columns = ['close', 'high', 'low', 'open', 'volume'])

    return OHLC

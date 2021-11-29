import datetime
import time
import pandas as pd
import finnhub

_api_key = 'bpu4no7rh5red6hq49u0'
_resolution = 'D'


class DataProvider:

    def __init__(self, exchange, symbol):
        self.client = finnhub.Client(api_key=_api_key)
        self.exchange = exchange
        self.symbol = symbol
        self.result = ''

    def getCryptoSymbols(self):
        self.result = self.client.crypto_symbols(exchange=self.exchange)
        return pd.DataFrame(self.result)

    def getCryptoSymbolCandles(self, symbol, _from, _to):
        self.result = self.client.crypto_candles(symbol=symbol, resolution=_resolution, _from=_from, to=_to)
        # print(self.result)
        return pd.DataFrame(self.result)

    def getPeriodicCryptoCandles(self, symbol, resolution, period):
        '''
        :param symbol:
        :param resolution:
            'D' for Day , '60' for hour, '30' for 30 minutes ,
            '15' for 15 minutes , '10' for 10 minutes , '5' for 5 minutes
        :param period: number of iterates to be returns
        :return:
        '''
        if resolution not in ['D', '60', '30', '15', '10', '5']:
            return 'Error in Resolution'
        if resolution == 'D':
            times = 24 * 60 * 60
        else:
            times = int(resolution) * 60
        _to = int(datetime.datetime.now().timestamp())
        _from = _to - (times * period)
        print(_to)
        print(_from)
        self.result = self.client.crypto_candles(symbol=symbol, resolution=resolution, _from=_from, to=_to)
        if self.result['s'] == 'ok':
            resultDF = pd.DataFrame(self.result)
            last_fetched_timestamp = resultDF.tail(1)['t']
            print(last_fetched_timestamp)
            print(_to)
            print(last_fetched_timestamp + times)
            next_period = last_fetched_timestamp + times
            print((last_fetched_timestamp + times) - _to)
            seconds_to_next_period = next_period - _to
            print('Sleep for {} seconds'.format(seconds_to_next_period))
            time.sleep(seconds_to_next_period)
            self.result = self.client.crypto_candles(symbol=symbol, resolution=resolution, _from=_to, to=next_period)
            if self.result['s'] == 'ok':
                resultDF = resultDF.append(pd.DataFrame(self.result), ignore_index=True)
                return resultDF
        else:
            return 'Error in fetching data'



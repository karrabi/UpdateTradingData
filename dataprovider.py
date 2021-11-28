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

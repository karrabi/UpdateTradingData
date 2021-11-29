import dataprovider as dp


def main():
    a = dp.DataProvider(exchange='BINANCE', symbol='BTCUSDT')
    # print(a.getCryptoSymbols())
    # print(a.getCryptoSymbolCandles(symbol='BINANCE:BTCUSDT', _from=1637608665, _to=1638127065))
    print(a.getPeriodicCryptoCandles(symbol='BINANCE:BTCUSDT', resolution='5', period=15))


if __name__ == '__main__':
    main()


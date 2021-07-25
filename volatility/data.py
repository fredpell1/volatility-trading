import pandas
import yfinance as yf

#get intra-day trading data
def get_yahoo_data_intraday(symbol,period,interval):
    stock = yf.Ticker(symbol.upper())
    dic = stock.history(period,interval)
    dic.symbol =symbol
    return dic

#get daily trading data
def get_yahoo_data_daily(symbol,period="max"):
    stock = yf.Ticker(symbol)

    dic =  stock.history(period)
    dic.symbol = symbol
    return dic 



#to use if you already have a csv file
def yahoo_helper(symbol, data_path, *args):
    """
    Returns DataFrame/Panel of historical stock prices from symbols, over date
    range, start to end. 
    
    Parameters
        ----------
        symbol : string
            Single stock symbol (ticker)
        data_path: string
            Path to Yahoo! historical data CSV file
        *args:
            Additional arguments to pass to pandas.read_csv
    """

    try:
        data = pandas.read_csv(
            data_path,
            parse_dates=['Date'],
            index_col='Date',
            usecols=[
                'Date',
                'Open',
                'High',
                'Low',
                'Adj Close',
            ],
            *args
        ).rename(columns={
            'Adj Close': 'Close'
        })

    except Exception as e:
        raise e

    data.symbol = symbol
    return data

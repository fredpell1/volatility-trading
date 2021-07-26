import pandas
import yfinance as yf

#test

#get intra-day trading data
def get_yahoo_data_intraday(symbol,period,interval):
    """
    Returns a pandas dataframe of historical stock price from symbols,
    over a day period and within an intraday interval. The data is taken from
    the Yahoo! finance website

    Parameters
        -----------
        symbol: String of the stock
        period: String day period, possible values:  1d, 5d, 1mo
        interval: String intraday interval, possible values: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h
    """
    stock = yf.Ticker(symbol.upper())
    df = stock.history(period,interval)
    df.symbol =symbol
    return df

#get daily trading data
def get_yahoo_data_daily(symbol,period="max"):
    """
    Returns a pandas dataframe of historical stock price from symbols,
    over a day period. The data is taken from the Yahoo! finance website

    Parameters
        -----------
        symbol: String of the stock
        period: String day period, possible values: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    """
    stock = yf.Ticker(symbol)

    df =  stock.history(period)
    df.symbol = symbol
    return df 



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

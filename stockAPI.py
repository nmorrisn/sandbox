"""this is a test"""
import re
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

def strip_number(text):
    """returns text stripped of leading numbers"""
    return re.sub("[0-9][0-9]. ", "", text)

class AlphaVantage():
    """docstring for alphaVantage."""
    def __init__(self, key):
        # Define globals
        self.url = "http://www.alphavantage.co/query?"
        self.key = key
        #super(alphaVantage, self).__init__()

    def __get_response(self, params):
        """invokes alpha vantage API call"""
        return requests.get(self.url + params + "&apikey=" + self.key).json()

    def get_quote(self, symbol):
        """gets quote for given symbol"""
        func = "GLOBAL_QUOTE"
        response = self.__get_response("function=" + func + "&symbol=" + symbol)

        payload = response["Global Quote"]

        if not payload:
            raise Exception("No results for ticker symbol: " + symbol)

        new_dict = {}

        for x, y in payload.items():
            new_dict[strip_number(x)] = y

        return new_dict

    def get_intraday(self, symbol, interval):
        """gets intraday series for given symbol"""
        func = "TIME_SERIES_INTRADAY"
        response = self.__get_response("function=" + func + "&symbol=" + symbol + "&interval=" + interval)

        payload = response["Time Series ("+interval+")"]
        return pd.DataFrame(data=payload)

    def get_daily(self, symbol):
        """gets daily series for given symbol"""
        func = "TIME_SERIES_DAILY"
        response = self.__get_response("function=" + func + "&symbol=" + symbol)

        payload = response["Time Series (Daily)"]
        df = pd.DataFrame(data=payload, dtype=np.float32)
        return df

    def plot_series(self, df):
        '''plots a line graph of the data from df'''
        df = df.T
        df.index = df.index.astype(np.datetime64)
        vol = df["5. volume"]
        df = df.drop(columns=["5. volume"])
        i = 0
        fig, axs = plt.subplots(4, 1, constrained_layout=True, sharex=True)
        for col in df.columns.values.tolist():
            axs[i].plot(df[col])
            axs[i].set_title(col)
            #df[col].plot.line()
            i += 1

        plt.figure(2)
        vol.plot()

        plt.xticks(np.arange(min(df.index), max(df.index), np.timedelta64(7,'D')))
        return fig

def main():
    """main"""
    stock = AlphaVantage(input("Enter API key: "))
    df = stock.get_daily("CGC")
    stock.plot_series(df)
    plt.show()


if __name__ == "__main__":
    main()

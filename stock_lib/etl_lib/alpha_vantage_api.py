import requests
import pandas as pd


class AlphaVantageApi():
    def __init__(self, function):
        self.valid_functions = ['TIME_SERIES_DAILY', 'TIME_SERIES_INTRADAY',
                                'TIME_SERIES_WEEKLY']
        self.api_key = "5Z1O"
        self.set_function(function)

    def get_data_as_dataframe(self, symbol, interval="1min",
                              outputsize='full'):
        data = self.get_data_as_json(symbol, interval, outputsize)
        df = pd.DataFrame.from_dict(data[list(data)[1]], orient='index')
        df.columns = [col[1].strip(" ") for col in df.columns.str.split(".")]
        return df.astype("float")

    def get_meta_data(self, symbol, interval="1min", outputsize='compact'):
        data = self.get_data_as_json(self.function, symbol, interval)
        return data['Meta Data']

    def get_data_as_json(self, symbol, interval="1min", outputsize='full'):
        url = self.make_api_url(symbol, interval, outputsize)
        api_connection = requests.get(url)
        data = api_connection.json()
        if 'Error Message' in data.keys():
            raise ValueError(data['Error Message'])
        else:
            return data

    def make_api_url(self, symbol, interval="1min", outputsize='full'):
        base_url = ("http://www.alphavantage.co/query?"
                    "function={0}&"
                    "symbol={1}&"
                    "interval={2}&"
                    "apikey={3}&"
                    "outputsize={4}").format(self.function, symbol,
                                             interval, self.api_key,
                                             outputsize)
        return base_url

    def set_function(self, function):
        if function.upper() not in self.valid_functions:
            raise ValueError("Function {} is not in the list "
                             "of supported functions.")
        else:
            self.function = function.upper()

import requests
import pandas as pd
import bs4
import numpy as np


class StockMeta():
    def __init__(self, exchange="sp_500"):
        self.set_exchange(exchange)

    def get_stock_meta_json(self):
        symbolslist = self.get_raw_symbols()
        stock_meta = []
        for i, symbol in enumerate(symbolslist):
            tds = symbol.select('td')
            stock_info = {"ticker": tds[0].text,
                          "name": tds[1].text,
                          "sector": tds[3].text,
                          "sub_sector": tds[4].text,
                          "date_added": tds[6].text
                          }
            stock_meta.append(stock_info)
        return stock_meta

    def get_stock_meta_df(self):
        symbolslist = self.get_raw_symbols()
        tickers = []
        names = []
        sectors = []
        sub_sectors = []
        date_added = []
        for i, symbol in enumerate(symbolslist):
            tds = symbol.select('td')
            tickers.append(tds[0].text),
            names.append(tds[1].text)
            sectors.append(tds[3].text)
            sub_sectors.append(tds[4].text)
            date_added.append(tds[6].text)
            input_data = np.transpose([tickers, names, sectors,
                                       sub_sectors, date_added])
        return pd.DataFrame(input_data,
                            columns=['ticker', 'name', 'sector', 'sub_sector',
                                     'date_added'])

    def get_raw_symbols(self):
        txt = self.get_text_data()
        soup = bs4.BeautifulSoup(txt,  "html5lib")
        symbolslist = soup.select('table')[0].select('tr')[1:]
        return symbolslist

    def get_text_data(self):
        return requests.get(self.web_url).text

    def set_exchange(self, exchange):
        if exchange.lower() == "sp_500":
            self.web_url = ('https://en.wikipedia.org/wiki/'
                            'List_of_S%26P_500_companies')
        else:
            raise ValueError("Exhange name '{}'' "
                             "not supported".format(exchange))

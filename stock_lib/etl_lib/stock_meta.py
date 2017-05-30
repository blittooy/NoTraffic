import requests
import pandas as pd
import bs4


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
        ticker_list = []
        name_list = []
        sector_list = []
        sub_sector_list = []
        date_added_list = []
        for i, symbol in enumerate(symbolslist):
            tds = symbol.select('td')
            ticker_list.append(tds[0].text),
            name_list.append(tds[1].text)
            sector_list.append(tds[3].text)
            sub_sector_list.append(tds[4].text)
            date_added_list.append(tds[6].text)
        return pd.DataFrame([name_list, sector_list,
                             sub_sector_list, date_added_list],
                            columns=['ticker', 'name', 'sector', 'sub_sector',
                                     'date_added_list'])

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

from pytrends.request import TrendReq

class Google:
    
    def __init__(self, query):
        self.query = query
        self.pytrend = TrendReq()

    def build_payload(self, cat=0, timeframe='today 12-m', geo='AR'):
        self.pytrend.build_payload(self.query, cat=cat, timeframe=timeframe, geo=geo)

    def get_data_trends(self):
        df_interest = self.pytrend.interest_over_time()
        return df_interest
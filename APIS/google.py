from pytrends.request import TrendReq

def get_datatrends():
    pytrend = TrendReq()
    query = ['dolar']
    pytrend.build_payload(query, cat=0, timeframe='today 12-m', geo='AR')
    df_interest = pytrend.interest_over_time()
    return(df_interest)
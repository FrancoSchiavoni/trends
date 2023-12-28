import requests
import pandas as pd


def get_dataframedolar():
    URL = 'https://api.bluelytics.com.ar/v2/evolution.json?days=360'
    json = requests.get(URL).json()
    df = pd.DataFrame(json)
    filtered_df = df[df['source'] == 'Blue']
    return(filtered_df)



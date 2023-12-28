import pandas as pd
import requests

class Dolar:

    def __init__(self, days=360, base_url='https://api.bluelytics.com.ar/v2/evolution.json?days='):
        self.url = f'{base_url}{days}'


    def get_data_frame_dolar(self):
        json_data = requests.get(self.url).json()
        df = pd.DataFrame(json_data)
        filtered_df = df[df['source'] == 'Blue']
        return filtered_df



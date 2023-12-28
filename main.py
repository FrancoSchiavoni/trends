import APIS.dolar as dolar
import APIS.google as google
from matplotlib import pyplot as plt
import pandas as pd

#Instance
dolar_instance = dolar.Dolar()
google_instance = google.Google(query=['dolar'])

#Get dataframe dolar Blue
df_blue = dolar_instance.get_data_frame_dolar()

#Get dataframe google Trends
google_instance.build_payload(cat=0, timeframe='today 12-m', geo='AR')
df_trends = google_instance.get_data_trends()



# columns 'date' type datetime64[ns]
df_trends.index = pd.to_datetime(df_trends.index)
df_blue['date'] = pd.to_datetime(df_blue['date'])

# column 'date' as index 
df_blue.set_index('date', inplace=True)


plt.plot(df_trends.index, df_trends['dolar'])
plt.plot(df_blue.index, df_blue['value_sell'])


# Añadir etiquetas y título
plt.xlabel('date')
plt.ylabel('value_sell/indice')
plt.title('Cotizacion Dolar - Tendencia')

# Mostrar el gráfico
plt.show()

import APIS.dolar as dolar
import APIS.trends as trends
from matplotlib import pyplot as plt
import pandas as pd

df_blue = dolar.get_dataframedolar()
df_trends = trends.get_datatrends()


# ambas columnas 'date' sean del tipo datetime64[ns]
df_trends.index = pd.to_datetime(df_trends.index)
df_blue['date'] = pd.to_datetime(df_blue['date'])

# columna 'date' sea el índice
df_blue.set_index('date', inplace=True)


plt.plot(df_trends.index, df_trends['dolar'])
plt.plot(df_blue.index, df_blue['value_sell'])


# Añadir etiquetas y título
plt.xlabel('date')
plt.ylabel('value_sell/indice')
plt.title('Cotizacion Dolar - Tendencia')

# Mostrar el gráfico
plt.show()

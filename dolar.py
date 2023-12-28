import requests
import pandas as pd
from matplotlib import pyplot as plt


URL = 'https://api.bluelytics.com.ar/v2/evolution.json?days=360'

json = requests.get(URL).json()
df = pd.DataFrame(json)
filtered_df = df[df['source'] == 'Blue']

print(filtered_df)



# Graficar usando Matplotlib
plt.plot(filtered_df['date'], filtered_df['value_sell'])

plt.gca().invert_xaxis()

# Añadir etiquetas y título
plt.xlabel('date')
plt.ylabel('value_sell')
plt.title('Cotizacion Dolar')

# Mostrar el gráfico
plt.show()



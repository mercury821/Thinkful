import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 



df = pd.read_csv('countries of the world.csv')

df = df.dropna()

df['Birthrate'] = df['Birthrate'].str.replace(',','.')

df['Birthrate'] = df['Birthrate'].apply(float)

plt.scatter(x = df['GDP ($ per capita)'], y = df['Birthrate'], color='black')
plt.title('Countries of the World Comparison')
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Birthrate')
plt.show()
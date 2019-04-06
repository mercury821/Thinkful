import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 



df = pd.read_csv('countries of the world.csv')

df = df.dropna()

df['Literacy (%)'] = df['Literacy (%)'].str.replace(',','.')

df['Literacy (%)'] = df['Literacy (%)'].apply(float)

plt.scatter(x = df['GDP ($ per capita)'], y = df['Literacy (%)'], color='blue')
plt.title('Countries of the World Comparison')
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')
plt.show()
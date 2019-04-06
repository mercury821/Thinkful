import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 



df = pd.read_csv('countries of the world.csv')

df = df.dropna()

df['Literacy (%)'] = df['Literacy (%)'].str.replace(',','.')

df['Literacy (%)'] = df['Literacy (%)'].apply(float)

df['Phones (per 1000)'] = df['Phones (per 1000)'].str.replace(',','.')

df['Phones (per 1000)'] = df['Phones (per 1000)'].apply(float)

plt.scatter(x = df['Phones (per 1000)'], y = df['Literacy (%)'], color='red')
plt.title('Countries of the World Comparison')
plt.xlabel('Phones')
plt.ylabel('Literacy (%)')
plt.show()
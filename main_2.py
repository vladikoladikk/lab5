import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#1
df = pd.read_csv('test.csv')

#2
df = df.sample(n=1000)

#3
print(f"\n\tData Omissions"
      f"\n{df.isnull().sum()}")

#4
plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
df['Square'].plot(kind='box', logy=True)
plt.title('Боксплот с логарифмической шкалой')

plt.subplot(1, 2, 2)  # Скорректированный индекс подграфика
df['Square'].plot(kind='hist', bins=30, logy=True)
plt.title('Гистограмма с логарифмической шкалой')

plt.show()

#5
numeric_columns = ['Square','LifeSquare','KitchenSquare','Healthcare_1']
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
df = df[(df['Square'] > 20) & (df['Square'] < 200)]

#6
print(f"\n\tNumber of Apartments by Number of Rooms"
          f"\n{df['Rooms'].value_counts()}")

#7
pivot_table = df.pivot_table(index='DistrictId', columns='Rooms', values='Id', aggfunc='count')
print(f"\n\tSummury Table"
      f"\n{pivot_table}")

#8
df.to_csv('krantsevich.csv',index=False)
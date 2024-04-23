from cv2 import rotate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('bikes.csv')

print("Print lima baris pertama")
print(data.head());

print("\nInformasi data frame")
print(data.info());

data['Bike Sold'] = pd.cut(data['Sold'], bins=[0, 30, 40, 50, np.inf], labels=['<30', '30-40', '40-50', '50+'])

count_sold = data['Bike Sold'].value_counts()


#?visualisation

plt.figure(figsize=(8,6))
sns.barplot(x=count_sold.index, y=count_sold.values)

plt.title('Jumlah bike di booking dalam category terjual')
plt.xlabel('Bike Sold')
plt.ylabel('Bike Sold Count')

average_sold = data.groupby('Nama')['Sold'].mean()

plt.figure(figsize=(10,6))
sns.barplot(x=average_sold.index, y=average_sold.values)
plt.title('Rata rata terjual per nama')
plt.xlabel('Nama')
plt.ylabel('Sold')
plt.xticks(rotation=45)
plt.show()
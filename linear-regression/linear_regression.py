import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('linear-regression/house.csv')


def convert_price(price):
    if pd.isna(price) or price == 'Call for Price':
        return None
    price = price.replace(',', '')
    if ' Lac' in price:
        return float(price.replace(' Lac', '')) * 100000
    elif ' Cr' in price:
        return float(price.replace(' Cr', '')) * 10000000
    else:
        return float(price)


def convert_area(area):
    if pd.isna(area):
        return np.nan
    if ' sqft' in area:
        return float(area.replace(' sqft', '').replace(',', ''))
    elif ' sqm' in area:
        return float(area.replace(' sqm', '').replace(',', '')) * 10.7639
    else:
        return np.nan


data['Amount(in rupees)'] = data['Amount(in rupees)'].apply(convert_price)
data['Carpet Area'] = data['Carpet Area'].apply(convert_area)


data = data.dropna(subset=['Amount(in rupees)', 'Carpet Area'])


X = data[['Carpet Area']]
y = data['Amount(in rupees)']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R^2) Score: {r2}")


print(f"Slope (b1): {model.coef_[0]}")
print(f"Intercept (b0): {model.intercept_}")


plt.scatter(X, y, color='blue', label='Data Aktual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Garis Regresi')
plt.xlabel('Carpet Area (sqft)')
plt.ylabel('Amount (in rupees)')
plt.title('Regresi Linear: Prediksi Harga Properti')
plt.legend()
plt.show()

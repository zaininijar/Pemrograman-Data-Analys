# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.naive bayes import GaussianNB
# from sklearn.metrics import accuracy_score, precision_score, recall_ score, confusion matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# # Load data
# data = pd.read csv('pr10 data.csv') # Ganti
# "data.csv'
# dengan nama file CSV Anda
# #Pisahkan fitur dan target
# X
# = data.drop ('target_column', axis=1) # Ganti 'target_column'
# dengan nama kolom target
# y
# = data[ 'target_column' ]
# #Bagi data menjadi data latih dan data uji
# X_train, X_test, y_train, y_test = train test split(X, y, test size=0.2, random state=42)
# #Inisialisasi dan latih model Naive Bayes
# model = GaussianNB()
# model.fit(X_train, y_train)
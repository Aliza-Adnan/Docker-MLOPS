# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:15:21 2023

@author: aliza
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
s=pd.read_csv('D:/Salary_Data.csv')
X_train, X_test, y_train, y_test = train_test_split(s['YearsExperience'], s['Salary'], random_state=1)
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

X_train=X_train.values.reshape(-1,1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test.values.reshape(-1,1))
print(y_pred)
pickle.dump(knn, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

#confusion_matrix(y_test, y_pred)
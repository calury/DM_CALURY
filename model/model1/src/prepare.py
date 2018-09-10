#-*- coding:UTF-8 -*-
"""模型数据预处理
"""
import os
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# load data

# filePath = r"E:/SPARKPATENT/src/DM_CALURY/model/model1"
filePath = os.path.abspath("..")
filename = filePath + os.sep + "DATA/pima-indians-diabetes.csv"
print(filename)
dataset = loadtxt(filename, delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))












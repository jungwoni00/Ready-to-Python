# -*- coding: utf-8 -*-
"""심장 질환 데이터 분석.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PhWUBSrYIpdLJPLwdllxJnWVQC6Gs98i
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
data = pd.read_csv(url, names=columns)


print(data.head())
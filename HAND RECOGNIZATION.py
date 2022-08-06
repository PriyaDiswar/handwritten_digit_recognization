import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
"""
Dataset is downloaded from given link:
https://www.kaggle.com/competitions/digit-recognizer/data?select=train.csv
"""

dataset=pd.read_csv("/home/hacquees/Pictures/C/train.csv").values

#print(dataset)
clf=DecisionTreeClassifier()

#Training to machine

x_train=dataset[:21000,1:]
x_train_label=dataset[:21000,0]
clf.fit(x_train,x_train_label)

#Testing to machine
x_test=dataset[21000:,1:]
x_test_label=dataset[21000:,0]

data=x_test[int(input())]
df=data.reshape(28,28)

plt.imshow(255-df,cmap="gray")
plt.axis("off")
print(clf.predict([x_test[int(input())]]))
plt.show()
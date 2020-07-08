import pandas as pd                      # this used for manipulation
import matplotlib.pyplot as plt          #this  used for visualization
import seaborn as sn                     #this used for advanced visualization
import warnings
import pickle
from sklearn.preprocessing import LabelEncoder         #this used for label encoding
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 

def flower_predict():
	df = pd.read_csv(r"C:\Users\preet\Downloads\Datasets (1)\final data set\iris.csv")
	label = LabelEncoder()
	label.fit_transform(df.variety)
	df.variety = label.fit_transform(df.variety)
	x = df[['sepal_length','sepal_width','petal_length','petal_width']] # Independent Var
	y = df['variety']                                                   #Dependent Var
	x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)
	x_train.shape
	x_test.shape
	svm = SVC(C=10,gamma='auto_deprecated')
	svm.fit(x_train,y_train)
	svm.score(x_train,y_train)
	yp = svm.predict(x_test)

	# Take input from user
	sepal_length = float(input("Enter sepal_length: "))
	sepal_width = float(input("Enter sepal_width: "))
	petal_length = float(input("Enter petal_length: "))
	petal_width = float(input("Enter petal_width: "))

	y = svm.predict([[sepal_length,sepal_width,petal_length,petal_width]])  # input must be 2D array
	print(y)

flower_predict()
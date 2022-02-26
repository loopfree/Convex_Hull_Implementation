import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import datasets

from myconvexhull import MyConvexHull

# Untuk checking hasil 
# from scipy.spatial import ConvexHull

if __name__ == "__main__":
	print("List dataset yang tersedia:")
	print("1. Iris")
	print("2. Wine")
	print("3. Breast Cancer")
	option = int(input("Input dataset yang diinginkan: "))

	if (option==1):
		data = datasets.load_iris()
		title = "Iris Dataset"
	elif (option==2):
		data = datasets.load_wine()
		title = "Wine Dataset"
	elif (option==3):
		data = datasets.load_breast_cancer()
		title = "Breast Cancer Dataset"
	else:
		print("Dataset tidak tersedia")
		exit()

	#create a DataFrame 
	df = pd.DataFrame(data.data, columns=data.feature_names) 
	df['Target'] = pd.DataFrame(data.target) 
	# print(df)
	df.head()
	plt.figure(figsize = (10, 6))
	colors = ['b','r','g', 'c', 'm', 'y', 'k', 'w', 'aquamarine', 'mediumseagreen']
	plt.title(title)
	plt.xlabel(data.feature_names[0])
	plt.ylabel(data.feature_names[1])
	for i in range(len(data.target_names)):
		bucket = df[df['Target'] == i]
		bucket = bucket.iloc[:,[0,1]].values
		# hull = ConvexHull(bucket)
		# print(bucket)
		hull = MyConvexHull(bucket)
		plt.plot(hull.x_coords, hull.y_coords, colors[i])
		plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
		# plt.plot(hull[0], hull[1], colors[i])
		# print(hull.simplices)
		# for simplex in hull.simplices:
		# 	print(simplex)
		# 	plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
	plt.legend()
	plt.show()
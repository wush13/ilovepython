
import numpy as np
import random
from collections import Counter
## initail pts randomly
def initialmatrix(n, m):
	matrix = np.random.rand(n,m) 
	print(matrix)
	return matrix

def initialpoint(m):
	pt = np.random.rand(m,1) 
	print(pt)
	return pt

def initiallabel(m, label_cnt):
	labels = []
	for i in range(m):
		labels.append(random.randint(1, label_cnt))
	print(labels)
	return labels

## calculate the distance between 2 points
def calcdist(p1, p2):
	dist = np.sqrt(np.sum(np.square(p1-p2)))
	return dist
	

def knn(new_pt, pts, labels, k):
	dict = {}
	index = 0
	for pt in pts:
		dist = calcdist(new_pt, pt)
		dict[str(index) + '^^' + str(labels[index])] = dist
		index = index + 1
	sorted(dict.items(), key=lambda d: d[1])
	print(dict)
	lt = list(dict.keys())
	lt = lt[0:k]
	print(lt)
	ele_cnt = {}
	for element in lt: 
		if element.split('^^')[1] in ele_cnt:
			ele_cnt[element.split('^^')[1]] += 1 
		else:
			ele_cnt[element.split('^^')[1]] = 1
	sorted(ele_cnt.items(), key=lambda d: d[1])
	return list(ele_cnt.keys())[0]

if __name__ == '__main__':
	matrix = initialmatrix(5,2)
	point = initialpoint(2)
	labels = initiallabel(5, 2)
	classification_result = knn(point, matrix, labels, 3)
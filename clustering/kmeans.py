import numpy as np
## initail pts randomly
def initialmatrix(n, m):
	matrix = np.random.rand(n,m)
	matrix = matrix * 100
	print(matrix)
	return matrix

## calculate the distance between 2 points
def calcdist(p1, p2):
	dist = np.sqrt(np.sum(np.square(p1-p2)))
	return dist
	

def kmeans(pts, k, maxiter):
	row_rand_array = np.arange(pts.shape[0])
	np.random.shuffle(row_rand_array)
	row_rand = pts[row_rand_array[0:k]]
	print(row_rand)
	cluster_j = np.zeros(len(pts))
	dist_j = np.zeros(len(pts))  ##float('inf')
	for index in range(len(dist_j)):
		dist_j[index] = 10000000
	for iter in range(maxiter):
		print("Iter:"+ str(iter))
		for i in range(0,len(pts)):
			for j in range(0, k):
				dist = calcdist(row_rand[j], pts[i])
				if dist < dist_j[i]:
					dist_j[i] = dist 
					cluster_j[i] = j
		print("cluster result")
		print(cluster_j)
		last_center = row_rand
		row_rand = 0 / row_rand
		cluste_cnt = np.zeros(k)
		##averge to update centers
		for index in range(0, len(cluster_j)):
			row_rand[cluster_j[index]] += pts[index]
			cluste_cnt[cluster_j[index]] += 1
		for index in range(0, k):
			row_rand[index] = row_rand[index]/cluste_cnt[index]
		print("new center")
		print(row_rand)
		##if centers are not updated, finish the clustering
		if((last_center==row_rand).all() == True):
			print("cluster finished")
			break

if __name__ == '__main__':
	matrix = initialmatrix(1000,3)
	kmeans(matrix, 4, 10)
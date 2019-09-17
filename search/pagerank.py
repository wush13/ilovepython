import numpy as np
## initail degree matrix randomly
def initialmatrix(n):
	matrix = np.random.randint(0, 100, (n,n))
	print(matrix)
	return matrix

def main(nodes_num):
	weights = np.ones(nodes_num) 
	x = initialmatrix(nodes_num)
	x=x-np.diag(np.diag(x))  
	print(x)
	x_normed = x / x.sum(axis=0)
	print(x_normed)
	iteration = 1
	while True:
		new_weights = np.dot(x_normed,weights)
		print("Iteration: "+ str(iteration))
		print(new_weights)
		if (new_weights - weights).max() <= 0.0001:
			break
		weights = new_weights
		iteration = iteration + 1

if __name__ == '__main__':
	main(10)
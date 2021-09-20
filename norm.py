import math
def euclidNorm(x):
	'''
	return \sqrt{\sum x_i ^2}

	inputs:
	x(vector): a vector in N—D
	outputs:
	scalar: the vector norm 
	'''

	sum_ = 0
	for i in range(len(x)):
		sum_ += (x[i] **2)
		return math.sqrt(sum_)


norm = euclidNorm([4,4]) #  pass a vector to the def function
print(euclidNorm([4/norm,4/norm]))  # the vector divided by the norms should be "1"

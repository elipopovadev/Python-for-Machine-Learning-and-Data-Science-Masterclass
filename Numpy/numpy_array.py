import numpy as np

# Numpy.array()
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)

matrix = [[1, 2, 3, 4], [3, 4, 5, 6], [6, 7, 8, 9]]

np_matrix = np.array(matrix)
print(np_matrix)  # 4 by 4 matrix


# Numpy.arange()
new_array = np.arange(0, 11)
print(new_array)

new_array2 = np.arange(0, 11, 2)
print(new_array2)


# Numpy.zeros()
zeros_array = np.zeros(5)
print(zeros_array)
zeros_array1 = np.zeros((5, 5))
print(zeros_array1)  # 5 by 5 matrix with zeros


# Numpy.ones()
ones_array = np.ones(5)
print(ones_array)
ones_array1 = np.ones((5, 5))
print(ones_array1)  # 5 by 5 matrix with ones


# Numpy.linspace()
array = np.linspace(0, 10, 5)  # [ 0. 2.5 5. 7.5 10. ]
print(array)
array1 = np.linspace(0, 5, 5)  # [ 0. 1.25  2.5  3.75  5. ]
print(array1)
array2 = np.linspace(0, 5, 6)
print(array2)  # [0. 1. 2. 3. 4. 5.]


# Create identity matrix
identity_matrix = np.eye(5)
print(identity_matrix)


# Return random samples from a uniform distribution over [0, 1)
var = np.random.rand(10)  # 10 numbers from 0 to 1
print(var)
var1 = np.random.rand(5, 4)  # matrix with 5 rows and 4 colums from 0 to 1
print(var1)


# Return a sample (or samples) from the "standard normal" distribution
var2 = np.random.randn(5, 4)
print(var2)


# Return random integers from "low"(inclusive) to "high"(exclusive)
var3 = np.random.randint(1, 11, 2)
print(var3)  # [10 8]
var4 = np.random.randint(1, 11, (2, 2))
print(var4)  # array 2 by 2

# The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value), to be able to generate a random number.
np.random.seed(42)
print(np.random.rand(4))

np.random.seed(42)
print(np.random.rand(4))  # tha same result like above


# reshape()
arr = np.arange(0, 25)
print(arr)
print(arr.reshape(5, 5))


# max() and min()
ranarray1 = np.random.randint(0, 10, 4)
print(ranarray1.max())
print(ranarray1.min())
print(ranarray1.argmin())  # get the index of min value
print(ranarray1.argmax())  # get the index of max value


# dtype
print(ranarray1.dtype)  # int32

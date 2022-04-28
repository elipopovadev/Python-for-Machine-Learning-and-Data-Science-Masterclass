import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)
print(zeros_array)

# Create an array of 10 ones
ones_array = np.ones(10)
print(ones_array)

# Create an array of 10 fives
fives_array = np.empty(10, dtype=np.int32)
fives_array.fill(5)
print(fives_array)

# Create an array of the integers from 10 to 50
integers_array = np.arange(10, 51)
print(integers_array)

# Create an array of all even integers from 10 to 50
even_array = np.arange(10, 51, 2)
print(even_array)

# Create a 3 by 3 matrix with values ranging from 0 to 8
my_matrix = np.arange(0, 9)
reshape_matrix = np.reshape(my_matrix, (3, 3))
print(reshape_matrix)

# Create a 3 by 3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# Generate random number between  0 and 1
random_number = np.random.rand(1)
print(random_number)

# Generate an array of 25 random numbers sampled from a standard normal distribution
st_normal_array = np.random.randn(25)
print(st_normal_array.reshape(5, 5))

# Create the following matrix
following_matrix = np.arange(0.01, 1.01, 0.01)
print(following_matrix.reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1
linearly_array = np.linspace(0, 1, 20)
print(linearly_array.reshape(4, 5))


# Crete the matrices shown below from "mat" matrix
mat = np.arange(1, 26).reshape(5, 5)
slice_of_array = mat[2:, 1:]
print(slice_of_array)
print(mat[3][4])
print(mat[0:3, 1])
print(mat[4:, ])
print(mat[3:, ])

# Get the sum of all the values in mat
print(mat.sum())

# Get the standard deviation of the values in mat
print(np.std(mat))

# Get the sum of all the columns in mat
print(mat.sum(axis=0))

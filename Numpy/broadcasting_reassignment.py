import numpy as np

myarray = np.arange(0, 11)
print(myarray)  # [ 0  1  2  3  4  5  6  7  8  9 10]

myarray[0:4] = 100  # Broadcasting reassignment. Be careful!
print(myarray)  # [100 100 100 100   4   5   6   7   8   9  10]

slice_of_array = myarray[0:5]
print(slice_of_array)  # [100 100 100 100  4]
print(myarray)  # [100 100 100 100   4   5   6  ]

slice_of_array[:] = 200
print(myarray)  # [200 200 200 200 200   5   6   7   8   9  10]


# To avoid above:
arr_copy = myarray.copy()  # NB!
slice_simple = arr_copy[0:5]
slice_simple[:] = 900
print(slice_simple)  # [900 900 900 900 900]
print(arr_copy)  # [900 900 900 900 900   5   6   7   8   9  10]
print(myarray)  # [200 200 200 200 200   5   6   7   8   9  10]

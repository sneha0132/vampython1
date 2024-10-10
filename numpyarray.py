# library name:- numpy
# Numpy:-1. It is used to work on large data set.
#        2. Range is too large.
#        3. High order function.
#        4. Array reshape.
#        5. Create N dimensional array.

# How to use numpy in python:- goto terminal -> pip install numpy.

import numpy as np

# assign array in numpy
myPercentage = np.array([1, 2, 3, 4])
# print(myPercentage)
# print(type(myPercentage))

# update the data in array
# myPercentage[0] = 9
# myPercentage[1] = 10

# by using for loop
# a = 9
# for data in range(0,4):
#     myPercentage[data]= a + data
# print(myPercentage)

# by using while loop
# a = 9
# for data in range(0,4):
#     myPercentage[data]= a + data
# b = 0
# while b < 4:
#     myPercentage[b] = a + b
#     b = b+1
# print(myPercentage)

# access the data from numpy array
# for data in range(0, 4):
#     print(myPercentage[data])

myFriends = np.array(["Shivangi", "Sneha", "Divyansh", "Suryansh"])
for name in myFriends:
    print(name)

# for alphabetically order
myFriends.sort()
print(myFriends)

# reverse by using while loop
# x = 3
# while x >= 0:
#     myFriends[x]
#     print(myFriends[x])
#     x= x-1







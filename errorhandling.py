#  Exception handling
#to find error- catch:

# 1. NAME ERROR
# print(x) -> gives NameError
# SOLUTION:-
# try:
#     print(x)
# except NameError:
#     print("x not defined")

# 2. ZERO DIVISION ERROR
# y= 1/0 
# print(y) -> Gives ZeroDivisionError
# SOLUTION:-
# try: 
#     y=1/0
#     print(y)
# except ZeroDivisionError:
#     print("zero divixion error")

# 3. VALUE ERROR
# a= "Sneha"
# b= int(a)
# print(b)
# SOLUTION:-
# try:
#     a= "Sneha"
#     b= int(a)
#     print(b)
# except ValueError:
#     print("String not cast in int")

# 4. FILE NOT FOUND ERROR
# import os
# os.remove("myfile.txt")
# # SOLUTION:-
# try:
#     import os
#     os.remove("myfile.txt")
# except FileNotFoundError:
#     print("file not found")

# 5.  INDEX ERROR
# myList= ["sneha", "Shivangi", "Tanya"]
# print(myList[4])
#SOLUTION:-
# try:
#     myList= ["sneha", "Shivangi", "Tanya"]
#     print(myList[4])
# except IndexError:
#     print("index out of range")

# 6. INDENTATION ERROR: ONLY CAN SOLVE MANUALLY
# x=5
# if x>5:
# print(x)
# else:
# print(x)
#SOLUTION:- (WITH TRY) CAN'T DO IT BY TRY
# try:
#     if x>5:
#         print(x)
#         else
#         print(x)
# except IndentationError:
#     print("Indentation Error")

#  TYPE ERROR
# x="sneha"
# y=4
# c=x+y
# print(c)
# SOLUTION:-
# try:
#     x="sneha"
#     y=4
#     c=x+y
# except TypeError:
#     print("concatenate only str")

# 7. FINALLY ALWAYS WORK
try:
    x="sneha"
    y=4
    c=x+y
except TypeError:
    print("concatenate only str")
finally:
    print("Always run")


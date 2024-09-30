#Dictionary:- it can store the data in key value pair [Identification of dictionary:- curly bracket, colon and coma]
# eg name:Sneha
# Types:- ordered
# 	      No duplicate
# 	      Changeable'
# syntax:- 
myInfo=  {"name"  : "Sneha Singhal",
		  "email" : "s@gmail.com",
		  "mobile": "9876489399",
		  "age"   :"21"}   #to change the name
# print(type(myInfo))
# print(myInfo["mobile"])

# To access specific data from dictionary
    # dict["key"]

# print(f" my name is {myInfo["name"]}, i am {myInfo["age"]} year old email {myInfo["email"]} and mobile no is {myInfo["mobile"]}")

# #access the complete dictionary key value
# for value in myInfo.values():
#     print(value)

#to change the name
# myInfo["name"]= "Gungun"
# print(myInfo["name"])

# myInfo.update({"gender":"female"})
# print(myInfo["gender"])
# myInfo.pop("name")

# Set:- It can store the multiple data. It can not be modified.  [Identification:- curly brackets]
# types:- 1.unordered
        # 2. no duplicate
        # 3. unchangeable
# eg.- 
# mySet = {"Sneha", "laxmi", "Gungun"}   
# print(mySet)
# mySet[0]= "Tanya"

# Tuple:- 
# Types:- # 1. ordered
          # 2. No duplicate
          # 3. Unchangeable
myTuple=("Sneha", "Laxmi", "Gungun")
print(myTuple)



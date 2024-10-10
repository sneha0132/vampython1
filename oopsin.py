# object oriented programming structure
# class:- syntax:- class<className>:#  --> statement
# class Sneha:
    # print("my name is sneha")
    # age = 21
    # email= "sneha@gmail.com"
# object creation:- syntax:- object:class= class()
# sneha:Sneha= Sneha()
# print(sneha.age)
# print(sneha.email)

# class with object and function
class Student:
    name="Sneha"
    email="sneha@gmail.com"
    def findMyAge(this, cY, bY):
        # this-> pass current class reference
        ageInYear = cY- bY
        print(ageInYear)
    def monthlyPocketMoney(this, wM):
        monthlyPocketMoney= 4*wM
        print(monthlyPocketMoney)
stu:Student= Student()
stu.findMyAge(2024,2003)
stu.monthlyPocketMoney(20)
    


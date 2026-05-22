#6.write a program to check whether student is pass or fail
marks=float(input("enter your marks:"))
if marks>=40:
    print("pass")
else:
    print("fail")


#7.write a program to check if age is eligible for voting 
age=int(input("Enter your age:"))
if age >=18 :
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


#8.write a program to check if a number is greater than 100
num = int(input("enter a number: "))
if num > 100:
    print("number is greater than 100")
else:
    print("number is less than 100")


#9.write a python program to compare two product prices and find one cheaper 
product1 = float(input("enter price of product 1 :"))
product2 = float(input("enter price of product 2 :"))

if product1 < product2:
    print("product 1 is cheaper")
else :
    print("product 2 is cheaper")


#10.write a python program to check if entered password length is valid 
password = input("enter your password:")
length = len(password)
if length >=8:
    print("password valid")
else: 
    print("password invalid")
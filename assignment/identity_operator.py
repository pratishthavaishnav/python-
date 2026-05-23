#21.Write a Python program to check if two variables refer to the same object.
a = [3,2,1]
b = a 
if a is b :
    print("have same object" )
else :
    print("different object")


#22.Write a Python program to check if two lists are identical objects or not.
a = [1,2,3]
b = a       #same object

if a is b :
    print("identical object")
else:
    print("diferent object")

c = [3,4,5]
d = [3,4,5]  #different value 

if c is d :
    print("identical object")
else:
    print("different object")

print("equal values :",c==d)
print("same memory location :", c is d )

#23.Write a Python program to check if a variable is None.
c=[1,2,3]

if c is None :
    print("empty")
else:
    print("not empty")

d = None
print(d)

#24.Write a Python program to check if two employee records point to same memory.
emp1 = {"id": 198, "name": "pratishtha"}
emp2 = emp1  

if emp1 is emp2:
    print("Both employee records point to the same memory")
else:
    print("They point to different memory locations")


#25.Write a Python program to check if two strings are the same object.
name1 = input("enter a name :")
name2 = input("enter a name :")

if name1 is name2 :
    print("same")
else:
    print("different") 

name1 = input("enter a name :")
name2 = name1

if name1 is name2 :
    print("same")
else:
    print("different") 


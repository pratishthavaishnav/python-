#16.Write a Python program to check if a product is available in stock list.
stock_list = ["milk","maida","powder","soda","essence","sugar"]

print("cream" in stock_list)
print("milk" in stock_list)

#17.Write a Python program to check if a student is in topper list.
topper_list=["harsh","pratishtha","lakshita","komal","nishi","palak"]

print("divesh" in topper_list)
print("pratishtha" in topper_list)


#18.Write a Python program to check if entered city is in allowed delivery list.
city_list = ["indore","bhopal","mumbai","pune","udaipur"]

city = input("enter your city :").lower()
if city in city_list:
    print("your city is available for delivery")
else:
    print("not available in your city")


#19.Write a Python program to check if username exists in database list.
database =["pratishtha","pvaishnav", "vaishnav" ]

username = input("enter a username: ").lower()

if username in database :
    print("username exists")
else:
    print("username is not available")


#20.Write a Python program to check if a subject is in student’s course list.
subject_list = ["english","dsa","oops","python","java"]

subject = input("enter a subject :").lower()

if subject in subject_list:
    print("available")
else:
    print("not available")
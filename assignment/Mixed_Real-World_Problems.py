#31.Write a Python program to calculate net salary after tax and bonus.
salary = float(input("Enter your salary: "))
tax_rate = float(input("Enter the tax rate (in percentage): "))
bonus = float(input("Enter your bonus amount: "))  

net_salary = salary - (salary * tax_rate / 100) + bonus 
print("Your net salary after tax and bonus is: ", net_salary)


#32.Write a Python program to check if user is eligible for discount using age and membership status.
age = int(input("Enter your age: "))
membership_status = input("Are you a member? (yes/no): ")

if age >= 60 and membership_status == "yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")


#33.Write a Python program to validate login using username, password, and role.

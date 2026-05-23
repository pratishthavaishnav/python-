#11.write a python program to login success (username and password correct)
username = str(input("enter a username upto 20 words :"))
password = str(input("enter a password upto 8 words :"))

if len(username) <= 20 and len(password) <=8 :
    print("successful login")
else:
    print("detail are invalid")

#12.Write a Python program to check scholarship eligibility (marks > 80 AND attendance > 75)
marks = float(input("enter your marks:"))
attendance = float(input("enter your attendence:"))

if marks > 80 and attendance > 75:
    print("you are eligible for scholarship")
else:
    print("you are not eligible")


#13.Write a Python program to check discount eligibility (age > 60 OR student = True)
age= int(input("enter your age:"))
student_input = input("are you a student? (True/False): ")

student = student_input.lower() == "true"

if age > 60 or student:
    print("you are eligible for discount")
else:
    print("you are not eligible for discount")

    
#14.Write a Python program to check exam eligibility (attendance ≥ 75 AND fees paid).
attendance = float(input("enter your attendance:"))
fee_input = input("have you paid the fees?(yes/no): ")
fees_paid = fee_input.lower() == "yes"

if attendance >= 75 and fees_paid:
    print("you are eligible for the exam")
else:
    print("you are not eligible for the exam") 


#15.Write a Python program to check loan approval (income > limit AND no loan default).
income = float(input("enter your income: "))
limit = 100000.00

loan_input =input("no loan default? (yes/no):")
no_loan_default = loan_input.lower() == "yes"

if income > limit and no_loan_default:
    print("loan approved")
else:
    print("loan rejected")
    

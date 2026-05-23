#26.Write a Python program to perform permission check using bitwise AND.
READ_PERMISSION = 4  #100
WRITE_PERMISSION = 2  #010
EXECUTE_PERMISSION = 1  #001

user_permission = int(input("Enter user permission (0-7): "))

required_permission = READ_PERMISSION & WRITE_PERMISSION & EXECUTE_PERMISSION
if user_permission & required_permission == required_permission:
    print("Permission granted.")
else:
    print("Permission denied.")


#27.Write a Python program to toggle system settings using XOR.
camera_setting = int(input("Enter current camera setting (0-15): "))
toggle_camera = int(input("Enter toggle camera value (0-15): "))

new_camera_setting = camera_setting ^ toggle_camera
print("camera setting after toggle:", new_camera_setting)


#28.Write a Python program to double a number using left shift.
number = 6
doubled_number = number << 1
print("doubled number:", doubled_number)


#29.Write a Python program to divide a number by 2 using right shift.
number = 10 
divided_number = number >> 2 
print("divided number:", divided_number)


#30.Write a Python program to check even or odd using bitwise AND.
number = 7
if number & 1:
    print("Number is odd.")
else:
    print("Number is even.")
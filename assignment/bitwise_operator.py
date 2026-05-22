#26.Write a Python program to perform permission check using bitwise AND.
READ_PERMISSION = 4  #100
WRITE_PERMISSION = 2  #010
EXECUTE_PERMISSION = 1  #001

user_permission = int(input("Enter user permission (0-7): "))
required_permission = 7

if (user_permission & required_permission) == required_permission:
    print("Permission granted.")
else:
    print("Permission denied.")


#27.Write a Python program to toggle system settings using XOR.

#regular expression
# pv005@gmail
# dob
# email 
import re
namere = r"^[A-Za-z0-9]+@[a-z]{2,}$"
name = "pv005@gmail.com"
if re.match(namere,name):
    print("Valid")
else:
    print("Invalid")
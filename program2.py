#write a program for calculate the sum of first and last 5 digit of a number
number = 12345
LastDigit = number % 10
FirstDigit = number // 10000
print("last digit :", LastDigit)
print("first digit :", FirstDigit)
Sum = LastDigit + FirstDigit
print("sum of first and last digit :", Sum)

import math

number = int(input("Enter the five digit number: "))
LastDigit = number % 10
lenofnum = 10**Floor(math.log10(number))
FirstDigit = number // lenofnum
print("last digit :", LastDigit)
print("first digit :", FirstDigit)
Sum = LastDigit + FirstDigit
print("sum of first and last digit :", Sum)

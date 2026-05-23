#bitwise operators
'''
AND(&) | OR(|) | XOR(^)
THESE OPERATORS WORK WITH TWO OPERANDS'''

#enter a number and check if it is even or odd using bitwise operator
num = int(input("Enter a number: "))
if num & 1 == 0:
    print("even")
else:
    print("odd")


'''
Rshift(>>) | Lshift(<<)| compliment(~)
THESE OPERATORS WORK WITH ONE OPERAND'''

n = 30 
u = 3
print(n >> u)  # Right shift


#write a program to calculate variance

#data
D1 = 5
D2 = 7
D3 = 9
D4 = 10
D5 = 14
D6 = 15

Avg = (D1 + D2 + D3 + D4 + D5 + D6) / 6
print("average :", Avg)
 
 #formula : variance = ((D1 - Avg)**2 + (D2 - Avg)**2 + (D3 - Avg)**2 + (D4 - Avg)**2 + (D5 - Avg)**2 + (D6 - Avg)**2) / 6
variance = ((D1 - Avg)**2 + (D2 - Avg)**2 + (D3 - Avg)**2 + (D4 - Avg)**2 + (D5 - Avg)**2 + (D6 - Avg)**2) / 6
print("variance :", variance)
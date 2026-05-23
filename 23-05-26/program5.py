'''
cat: furniture
state: california
calculate total profit, quantity , sales
'''
#import required library
import openpyxl

# load workbook
wb = openpyxl.load_workbook(r"C:\Users\DELL\OneDrive\Desktop\python\Superstore-1.xlsx")
sheet = wb["Orders"]

total_profit = 0
total_quantity = 0
total_sales = 0

for data in sheet.iter_rows(min_row=2, values_only=True):
    if data[14] == "Furniture" and data[10] == "California":
        total_profit += data[20] or 0
        total_quantity += data[18] or 0
        total_sales += data[17] or 0

print(f"Total profit: {total_profit}")
print(f"Total quantity: {total_quantity}")
print(f"Total sales: {total_sales}")

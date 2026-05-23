'''
cat: furniture
state: california
calculate total profit, quantity , sales
'''

#import required library
import openpyxl

#load workbook
wb = openpyxl.load_workbook("C:\Users\DELL\OneDrive\Desktop\python\dataset\Superstore-1.xlsx")

sheet = wb["Orders"]

for data in sheet.iter_rows(max_row=3, values_only=True):
    print(data[14])
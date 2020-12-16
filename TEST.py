import xlrd
import openpyxl
wb = openpyxl.load_workbook('ss.xls',data_only = True)

workbook = xlrd.open_workbook('ss.xls')
worksheet = wb.worksheets[0]
# a = worksheet.cell_value(32, 1)
print(worksheet['B33'])

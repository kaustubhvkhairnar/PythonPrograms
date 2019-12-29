import pandas as pd

border = "-"*50

excel_file = 'Batch.xlsx'
batches = pd.read_excel(excel_file)
print()
print(batches.head())
print()

print(border)

print()    
batches_sheet1 = pd.read_excel(excel_file,sheet_name = 0,index_col = 0) #to print normally use index =0,index_col = 0 displays the zeroth column first 
print(batches_sheet1.head())
print()

print(border)

print()
xlsx = pd.ExcelFile(excel_file)
batches_sheets = []

for sheet in xlsx.sheet_names:
    print(sheet)
    batches_sheets.append(xlsx.parse(sheet))
    
batches = pd.concat(batches_sheets)
print(batches)


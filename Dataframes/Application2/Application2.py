import pandas as pd;
border = '-'*50
print(border)
print("Dataframe with list as dictionary2")
print()
data = [{'Name':'PPA','Duration':5,'Fees':11000},{'Name':'LB','Fees':9000},{'Name':'PYTHON','Duration':4,'Fees':7500}]
df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('AdmissionDetails.xlsx',engine = 'xlsxwriter')
df.to_excel(writer,sheet_name = 'Sheet1')
writer.save()
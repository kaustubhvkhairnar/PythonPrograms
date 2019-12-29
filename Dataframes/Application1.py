import pandas as pd;
border = '-'*50
print(border)
#######################################################
print(border)
print("Empty Dataframe")
print()
df = pd.DataFrame()
print(df)
print()
print(border)
########################################################
print(border)
print("Dataframe with list")
print()
data = [['PPA',3],['LB',3],['PYTHON',2],['ANGULAR'],['MULTIOS',3]]
df = pd.DataFrame(data,columns=['Name','Duration'])
print(df)
print()
print(border)
##########################################################
print(border)
print("Dataframe with list as dictionary1")
print()
data = {'Name':['PPA','LB','PYTHON','ANGULAR','MULTIOS'],'Duration':[3,3,2,0,3]}
df = pd.DataFrame(data)
print(df)
print()
print(border)
###########################################################
print(border)
print("Dataframe with list as dictionary2")
print()
data = [{'Name':'PPA','Duration':5,'Fees':11000},{'Name':'LB','Fees':9000},{'Name':'PYTHON','Duration':4,'Fees':7500}]
df = pd.DataFrame(data)
print(df)
print()
print(border)
############################################################
print(border)
print("DataFrame using series")
print()
df = {'One':pd.Series([1,2,3],index=['a','b','c']),'Two':pd.Series([4,5,6],index=['x','y','z'])}
print("One")
print(df['One'])
print()
print("Two")
print(df['Two'])
print()
################################################################








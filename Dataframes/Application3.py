import pandas as pd
import numpy as np

border = "-"*50

print("Empty Series")
s = pd.Series()
print(s)
print()
print(border)

#######################################
print("As List")
print()
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s[0])
print()
print(border)

#######################################
print("As array")
print()
data = np.array(['a','b','c','d'])
s = pd.Series(data,index = [100,101,102,103])
print(s[100])
print()
print(border)

########################################
print("As dictionary")
print()
data = {'a':0.1,'b':0.2,'c':0.3,'d':0.4}
s = pd.Series(data)
print(s)
print()
print(border)
print()
######################################
print("Another Format")
s = pd.Series([100,101,102,103],index = ['a','b','c','d'])
print(s['a'])
print()
print(border)
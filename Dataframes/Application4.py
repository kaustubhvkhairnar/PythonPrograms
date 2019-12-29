#This application won't work on versions after 2.7

import pandas as pd
import numpy as np


df1 = {'One':pd.Series([1,2,3],index=['a','b','c']),'Two':pd.Series([4,5,6],index=['x','y','z'])}
df2 = {'One':pd.Series([23,5,4],index=['f','h','a']),'Two':pd.Series([8,9,7],index=['e','c','v'])}

data = {'ITEM1':df1,'ITEM2':df2}

p = pd.Panel(data)
print(p)
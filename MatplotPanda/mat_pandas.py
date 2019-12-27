import pandas as pd;
import matplotlib.pyplot as plt;

excel_file = "Matplot_Pandas.xlsx"
data = pd.read_excel(excel_file)
print()
print("print all data");
print(data)
print()
print("First 5 rows from file");
print(data.head())
print()
print("First 2 rows from file");
print(data.head(2))
print()
print("rows,columns");
print(data.shape)
print()
print("Sorted data");
sorted_data = data.sort_values(['Name'],ascending = False);
print(sorted_data)
print()
data['Age'].plot(kind = "hist");
plt.show();

data['Age'].plot(kind = "barh");
plt.show();

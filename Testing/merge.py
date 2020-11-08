import pandas as pd
from time import sleep 

print("Welcome to Excel worksheet merger")
print("All files must me .xlsx file format")
print("Please add the following answers")
print("........................................")
sleep(1)
file1 = input("Please enter the 1st excel file name\n")
file2 = input("Please enter the 2nd excel file name\n")
excel1 = file1 
excel2 = file2 
# excel1 = file1 + ".xlxs"
# excel2 = file2 + ".xlxs"
# excel3 = 'temperature_wurzburg.xlsx'
# excel4 = 'weight_wurzburg.xlsx'

print(excel1)
print(excel2)


df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)
# df3 = pd.read_excel(excel3)
# # df4 = pd.read_excel(excel4)

merge = pd.merge(df1, df2, on="timestamp")

print(merge)

merge.to_excel("Temp&Humi.xlsx")






# import pandas as pd

# excel1 = 'flow_wurzburg.xlsx'
# excel2 = 'humidity_wurzburg.xlsx'
# excel3 = 'temperature_wurzburg.xlsx'
# excel4 = 'weight_wurzburg.xlsx'


# df1 = pd.read_excel(excel1)
# df2 = pd.read_excel(excel2)
# df3 = pd.read_excel(excel3)
# df4 = pd.read_excel(excel4)

# merge = pd.merge(df1, df2, df3, df4, on="timestamp")

# print(merge)

# merge.to_excel("output.xlsx")

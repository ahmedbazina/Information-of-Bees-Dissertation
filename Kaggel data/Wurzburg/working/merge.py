import pandas as pd
from time import sleep 

print("Welcome to Excel worksheet merger")
print("All files must be .xlsx file format in order for the program to work")
print("Please answer the following>>")
print("........................................")
sleep(1)
file1 = input("Please enter the 1st excel file name:\n")
file2 = input("Please enter the 2nd excel file name:\n")

print("........................................")
sleep(1)
print("<<<<<<<<<<Files read sucessfully>>>>>>>>>>")
# print(excel1)
# print(excel2)
# print("" + file1 +".xlsx")

print("<<<<<<<<<<We are combining " + file1 + " & " + file2 + ">>>>>>>>>>")
print("<<<<<<<<<<Putting values into dataframe>>>>>>>>>>")
df1 = pd.read_excel("" + file1 +".xlsx")
df2 = pd.read_excel("" + file2 +".xlsx")

output = input("Please enter the output file name:\n")
print("........................................")

print("<<<<<<<<<<Merging the 2 files into 1 excel sheet based on timestamps matching>>>>>>>>>>")
merge = pd.merge(df1, df2, on="timestamp") # how="outer"


print(">>>>>>>>>>Exporting the data to an excel sheet named " + output + ">>>>>>>>>>")
merge.to_excel("" + output +".xlsx", index=False)

print(">>>>>>>>>>Excel worksheet has been sucessfully exported," "Check your folder", sep="_____"">>>>>>>>>>")
print("........................................")

# total_rows = merge.sum(axis=1)
# print(total_rows)



# Remove unwanted columns before exporting
# check duplicated data and remove it (if needed) Check
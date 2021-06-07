import pandas as pd
from time import sleep, time 

print("Welcome to Excel worksheet merger")
print("All files must be .csv file format in order for the program to work")
print("Please answer the following>>")
print("........................................")
sleep(1
)# Start timer
start = time()

# Asking user for file names
file1 = input("Please enter the 1st excel file name:\n")
file2 = input("Please enter the 2nd excel file name:\n")

print("........................................"
)sleep(1)
print("<<<<<<<<<<Files read sucessfully>>>>>>>>>>")
# print(excel1)
# print(excel2)
# print("" + file1 +".csv")

# Combining files asked for and putting them in a dataframe
print("<<<<<<<<<<We are combining " + file1 + " & " + file2 + ">>>>>>>>>>")
print("<<<<<<<<<<Putting values into dataframe>>>>>>>>>>")
df1 = pd.read_csv("" + file1 +".csv")
df2 = pd.read_csv("" + file2 +".csv")

# Asking user to name the output file
output = input("Please enter the output file name:\n")
print("........................................")

# Merging the files into 1 dataframe
print("<<<<<<<<<<Merging the 2 files into 1 excel sheet based on timestamps matching>>>>>>>>>>")
# how="outer" will add everything from both csv's this will include timestamp with no data i.e
# temp and humi results in 958884 on the other hand when not using outer and using inner 
# we get 271034 saving us 687850 of empty data not needed.
merge = pd.merge(df1, df2, on="timestamp") 

# Exporting the merged dataframe to new excel worksheet
print(">>>>>>>>>>Exporting the data to an excel sheet named " + output + ">>>>>>>>>>")
merge.to_csv("" + output +".csv", index=False)
print("<<<<<<<<<<Excel worksheet has been sucessfully exported, Check your folder>>>>>>>>>>")

# Stop the timer & round it to 1 decimal place
stop = time()
total = round(stop - start, 1)
print("Total time taken in seconds: ", total)
print("........................................")
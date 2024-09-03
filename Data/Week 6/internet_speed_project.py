#                                     Activity 1


#                       Mean of upload & download speeds

import pandas as pd

# df = pd.read_excel("results2024-9-3-1034.xlsx")
# print (df)

# #                       Isolates column "Download" & "Upload" to find mean

# # print (df["Download (Mb/s)"].mean())

# # print (df["Upload (Mb/s)"].mean())

# #                       Median of upload & downloads speeds

# #                       provides stats (50%=median)
# print(df.describe())


# #                   Sort data by slowest to fastest upload speed

# print (df["Upload (Mb/s)"].sort_values())

# #                   Sort data by fastest to slowest upload speed

# df = ("Upload (Mb/s").sort_values(reversed=True)
# print(df)

#                   Return download speeds faster than mean


#______________________________________________________________________
                
#                                         Activity 2

#download and save excel document, upload excel file onto python

df = pd.read_excel("group_results (1).xlsx")
print(df)

print(df.describe())

#          Data cleaning
#       ? removal of column "Package (if known)"" unrequired data
#df=df.drop(columns=["Package (if known)"])
#        incorrect ? removes "Internet service provider" column and changes values ? 

#        ? Truncated, convert wide to tall ? 
#        ? convert all values to same decimal place ?
#        ? arrange "Internet service providers" in alphabetical order so same providers grouped together ? 









import pandas as pd
import numpy as np

languages = pd.Series(["python","javascript","java","SQL"])
# print (languages)

# numbers = pd.Series([3,1,2,4])
# print (numbers)

# df = pd.DataFrame([("Anne", 30,"cat"),("Bill", 27,"dog"),("Steve",55,"fish")],
#                   columns=["name","age","pet"])
# print(df)

# positions = pd.Series([3,1,2,4])
# print(positions)

# df = pd.DataFrame({
#          "languages":languages,
#          "positions":positions
#  })

# print(df)

# print("_________")
# df.loc[4] = ["PHP",11]
# print(df)

# df.loc[3.5] = ["KESL",20]
# df = df.sort_index()
# print(df)

# #add new column of data
# df["Rankings 2022"] =[4,1,2,3,10,15]
# df["Rankings 2020"] = [5,10,45,20,7,8]
# df["Rankings 2019"] = [8,9,3,4,3,7]
# #insert a column to specific index
# df.insert(3,"Rankins 2021",[6,7,9,3,9,2])

# df.rename(columns={"positions" : "Rankings 2023"}, inplace=True)
# print(df)





# df = pd.DataFrame([("cath","coke",1.5),("ted","crisps",0.5),("sid","nuts",1.0)],
#                   columns=["name","order","cost"])

# print(df)

# df = pd.read_csv("speeds_1.csv")
# # print(df)

# df = pd.read_excel("speeds.xlsx")
# print(df)

#Activity 1 -week 5 (dataframe)

planet = pd.Series(["Earth","Jupiter","Venus","Neptune","Mars"])
print (planet)

temp = pd.Series([15,-110,464,-200,-65])
print (temp)

radius = pd.Series([6.4,69.9,6.1,24.6,3.4])
print (radius)

colour = pd.Series(["blue","yellow","brown","blue","red"])
print (colour)

feature = pd.Series(["water","largest","hottest","ice","volcanos"])
print (feature)

df = pd.DataFrame({
     "planet":planet,
     "temp":temp,
     "radius":radius,
     "colour":colour,
     "feature":feature
     })
print(df)

# Activity 3

df.insert(5,"discovered by",("adam","ant","amanda","amy","abi")),
df.insert(6, "year discovered",[1990,1980,1970,1960,1950]),
df.insert(7, "elements",("carbon","oxygen","zinc","hydrogen","phosphorus"))
print(df)




# #Activity 2 - convert data frame to excel
# df.to_excel(output.xlsx)

#Activity 2 (week5) slice notation

df = df.set_index("planet")
print(df.loc["Jupiter":"Neptune"])

#Activity 3 (week5)






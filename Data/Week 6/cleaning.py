import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

#df.info()

# #print(df.describe())

df = df.set_index("Transaction ID")

# #print(df)

# #df.info()

df = df.drop(columns=["Till ID","Unnamed: 0"])

# #print(df)

df = df.dropna(how="any")
# #print(df)

df = df.drop_duplicates()
df.at[15.0,"Cost"] = 6.00
#print(df)

#change time from 9.05 to 09:05
 

#df["Time"] = df["Time"].apply(float_to_time)
#df["Time"] = pd.to_datetime(df["Time"])
#print(df)

#search for most common item, does't work due to data type
#print(df["Basket"].value_counts())

def split_basket(string):
    items = string.split(',')
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

print(df["Basket"])
()
tall_basket = df.explode("Basket")
print (tall_basket)

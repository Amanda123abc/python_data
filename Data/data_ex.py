import pandas as pd

df = pd.read_csv("results.csv")

print(df["tournament"].nunique())




# #python ./data_ex.py 

# print(df.info())
# print(df.describe())

# df = pd.read_csv("spotify_songs(1).csv")
# print(df)

#will tell us size of dataset in rows and columns
#print(df.shape)

#will tell us name of the columns in dataset
#print(df.columns)

# print(df["playlist_genre"].value_counts())

# print(df["playlist_genre"].mode())









#pandas 

import pandas as pd 

df = pd.read_csv("tutorials/tuneindex.csv")

# print(df.head(10))

# df.info()
# print (df. head())
# print (df. describe())
# print("____")
# print (df["title"])
# print (df[["title","alt_title","downloaded"]])
# print ("downloaded")
# print (df[df[ "downloaded"] > 1000])


# mask = df["title"].str.contains("Whistle")
# filtered = df[mask]
# print(filtered)

# print(filtered["title"])
# s = "Hello"

# print(s.startswith("He"))

# print(df[df["title"].str.startswith("The")]["title"])
print(df[df["title"].str.endswith("Spear")][["title","tune_type", "downloaded"]])
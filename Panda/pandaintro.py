import pandas as pd

df1 = pd.DataFrame([[2,4,6],[10,20,30]],columns=["price","age","value"],index=["First","Second"])
print(df1)
print("\n")
print(df1.mean())
print("\n")
print("The mean is: %f" %df1.mean().mean())

#.read_csv("name","sep =")
#.read_excel("name", sheetname = #)

df2 = pd.read_json("supermarkets.json")
print(df2)

#header = None
#df2.columns = []
#df2.set_index("name", inplace = True, drop = False)
#df3 = df2.set_index("name", inplace = True)
#df2.loc[row:row. col:col] iloc for indices
#df2.drop("Name", 1=col, 0 = row)

#df2["New Col"] = df2.shape[0]*["Value"]

#df2_t = df2.T
#df2_t["xxx"] = ["df", "sdf", "sdfes", ...]
#df2 = df2_t.T
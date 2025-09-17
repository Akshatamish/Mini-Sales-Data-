import pandas as pd 
df=pd.read_csv("data.txt") # Load dataset
print(df)
df.to_excel("data.xlsx",index=False) #save dataset into excel file
# print("File converted succesfully")
print(df.head())

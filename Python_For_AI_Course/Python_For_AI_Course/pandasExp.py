import pandas as pd

csv_path= "D:/HOMEWARE/Projets/Python_For_AI_Course/data.csv"
df= pd.read_csv(csv_path)
#watch the ten first rows
print(df.head())

song={'album':['thriller','black','gttt'], 'released':[1987,1987,800], 'length':['00:42','28:98','89:23']}

dtframe= pd.DataFrame(song)
print(dtframe.head())

#creation d'un nouveau data frame avec la colonne 'released'
x=dtframe[['released']]
print(x)

#avec deux colonnes
xx =dtframe[['album','released']]
print(xx)

#filtrer les elements uniques d'une colonne
print(dtframe['released'].unique())

print(dtframe['released']>1900)

#selection des lignes pour lesquelles released >1900
print(dtframe[dtframe['released']>1900])

#save as a csv
dtframe.to_csv("D:/HOMEWARE/Projets/Python_For_AI_Course/dtframe.csv")


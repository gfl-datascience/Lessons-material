import pandas as pd
import numpy as np
df = pd.read_csv("house.csv")

df2 = df[["price","bedrooms","bathrooms","sqft_living","sqft_lot","floors","sqft_above","sqft_basement","yr_built","yr_renovated","city"]]
print(df2)
avg_price = np.mean( np.array(df2['price']) )
#print(avg_price)

df3 = df2.groupby(["city"]).mean()
df3 = df3.sort_values(by='price')
#print(df3)

max = np.max( np.array(df3['price']))
min = np.min( np.array(df3['price']))
#print("max is : "+str(int(max))+ " min is : "+str(int(min)))

sqft_total = df["sqft_above"]+df["sqft_basement"]
df["sqft_total_2"]=sqft_total

df['sqft_total'] = df.loc[0:100,['sqft_above','sqft_basement']].sum(axis=1)
df.to_csv("new_house.csv")
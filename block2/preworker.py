import numpy as np
import pandas as pd

df = pd.read_csv("AB_NYC_2019.csv")
df = df['price']
df.to_csv('prices.txt', index=False, sep='\n', header = False)

#print('classical mean is ' + str(np.mean(df)))
#print('classical var is ' + str(np.var(df)))
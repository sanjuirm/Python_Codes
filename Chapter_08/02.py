import pandas as pd
import numpy as np

# Creating a table
df = pd.DataFrame(index= list(range(0,51,5)) , columns= range(-20, 61, 10) )
df.index.rename('Wind_Speed', inplace= True)

for i in range(len(df.index)):
    if df.index[ i ] > 3:
        for j in range(len(df.columns)):
            t = df.index[ i ]
            v = df.columns[ j ]
        
            df.iloc[ i, j ] = np.round(35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + (0.4275 * t) * (v ** 0.16))
    else:
        print('next')

print(df.fillna('0'))
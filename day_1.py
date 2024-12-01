import numpy as np
import pandas as pd

df = pd.read_csv('input_day_1.txt', sep='\s+', header=None)

col_0 = np.sort(df[0].values)
col_1 = np.sort(df[1].values)

difference = col_0 - col_1

print(np.sum(difference))
import pandas as pd
import numpy as np
df = pd.read_csv("Data.csv")
print df.head()
print df["DELAY"]

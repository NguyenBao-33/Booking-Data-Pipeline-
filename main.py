import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "score": [80, 90, 75]
})

print(df)
print("Mean:", np.mean(df["score"]))
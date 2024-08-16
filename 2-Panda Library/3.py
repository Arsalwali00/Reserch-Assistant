import numpy as np
import pandas as pd

newdf=pd.DataFrame(np.random.rand(334,5), index=np.arange(334))

print(newdf)
print(type(newdf))

print(newdf.describe())
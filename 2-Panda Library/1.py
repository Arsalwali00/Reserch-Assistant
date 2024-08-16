import numpy as np
import pandas as pd

dict1= {

    "name":['Arslan','Luqman','Azfar'],
    "marks":[92,34,56],
    "city":['Jalalabad','Astore','Bagorte']
}

df=pd.DataFrame(dict1)
# print(df)

df.to_excel('arsal.xlsx', index=False)

# print(df.head(1)) show upper entries
# print(df.tail(1)) show last entries

# print(df.describe()) find out the statical data of above entries

arsal=pd.read_excel('read.xlsx')
print(arsal)


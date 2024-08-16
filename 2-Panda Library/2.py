import pandas as pd

# Creating a DataFrame
data = {'Lake': ['Lake1', 'Lake2', 'Lake3'],
        'Area': [150, 300, 500],
        'Risk_Level': ['Low', 'Medium', 'High']}
df = pd.DataFrame(data)

df.to_excel('lake.xlsx', index=False)
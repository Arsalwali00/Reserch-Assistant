import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import plotly.express as px



# Creating a DataFrame
data = {'Lake': ['Lake1', 'Lake2', 'Lake3'],
        'Area': [150, 300, 500],
        'Risk_Level': ['Low', 'Medium', 'High']}
df = pd.DataFrame(data)

# Since `Risk_Level` is categorical, it doesn't contribute to correlation calculations.
# We'll only use the `Area` for correlation, which doesn't make much sense on its own.
# Instead, we'll skip the heatmap as it won't be useful here.

# However, if you had more numerical data, you could use:
# sns.heatmap(df.corr(), annot=True)
# plt.show()

# Histogram of Lake Areas
df['Area'].hist(bins=5)
plt.xlabel('Area (sq km)')
plt.ylabel('Frequency')
plt.title('Distribution of Lake Areas')
plt.show()

fig = px.scatter(df, x='Area', y='Risk_Level', title='Interactive Risk Level vs. Area')
fig.show()
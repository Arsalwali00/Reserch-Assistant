
import matplotlib.pyplot as plt
import pandas as pd

# Creating a DataFrame
data = {'Lake': ['Lake1', 'Lake2', 'Lake3'],
        'Area': [150, 300, 500],
        'Risk_Level': ['Low', 'Medium', 'High']}
df = pd.DataFrame(data)


# Line plot
plt.plot(df['Lake'], df['Area'])
plt.xlabel('Lake')
plt.ylabel('Area')
plt.title('Lake Area Comparison')
plt.show()

# Bar plot
df.plot(kind='bar', x='Lake', y='Area', title='Lake Area Comparison')
plt.show()

# Scatter plot
plt.scatter(df['Area'], df['Risk_Level'])
plt.xlabel('Area')
plt.ylabel('Risk Level')
plt.title('Risk Level vs. Area')
plt.show()


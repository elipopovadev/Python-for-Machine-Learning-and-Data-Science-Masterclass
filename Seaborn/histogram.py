import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Create histogram
sns.set(style='darkgrid')
plt.figure(figsize=(5, 8), dpi=200)
df = pd.read_csv("C:/Users/eli/Desktop/dm_office_sales.csv")
distribution = sns.histplot(data=df, x='salary', bins=10,
                            color='red', edgecolor='blue', linewidth=4, kde=True)
print(distribution)

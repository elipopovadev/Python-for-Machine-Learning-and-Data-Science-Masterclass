import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 4), dpi=200)
df = pd.read_csv("C:/Users/eli/Desktop/dm_office_sales.csv")
plot1 = sns.scatterplot(x='salary', y='sales', data=df, style='level of education',
                        hue='level of education', palette=('Dark2'), s=200, alpha=0.2)
print(plot1)

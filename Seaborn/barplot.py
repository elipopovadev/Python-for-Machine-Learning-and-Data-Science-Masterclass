import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Create barplot
sns.set(style='darkgrid')
plt.figure(figsize=(10, 4), dpi=200)
df = pd.read_csv("C:/Users/eli/Desktop/dm_office_sales.csv")
barplot = sns.barplot(data=df, x='level of education',
                      y='salary', estimator=np.mean, ci='sd', hue='division')
plt.legend(bbox_to_anchor=(1.05, 1))
print(barplot)

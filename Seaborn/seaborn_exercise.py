import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/eli/Desktop/application_record.csv')

# Recreate the Scater Plot shown below
new_df = df.copy()
new_df = new_df[new_df['DAYS_EMPLOYED'] < 0]
new_df['DAYS_EMPLOYED'] = -1 * new_df['DAYS_EMPLOYED']
new_df['DAYS_BIRTH'] = -1 * new_df['DAYS_BIRTH']

plt.figure(figsize=(10, 8), dpi=200)
plot1 = sns.scatterplot(x='DAYS_BIRTH', y='DAYS_EMPLOYED',
                        data=new_df, linewidth=0, alpha=0.01)
print(plot1)

# Recreate the Distribution Plot shown below
new_df['Age in Years'] = new_df['DAYS_BIRTH'] / 365
sns.set(style='darkgrid')
plt.figure(figsize=(10, 8), dpi=200)
distribution = sns.histplot(data=new_df, x='Age in Years',
                            color='red', linewidth=2, edgecolor='black', kde=True)
print(distribution)

# Recreate the Categorical Plot shown below
plt.figure(figsize=(12, 5))
bottom_half_income = df.nsmallest(
    n=int(0.5*len(df)), columns='AMT_INCOME_TOTAL')
box_plot = sns.boxplot(x='NAME_FAMILY_STATUS', y='AMT_INCOME_TOTAL',
                       data=bottom_half_income, hue='FLAG_OWN_REALTY', linewidth=3)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2,
           borderaxespad=0., title='FLAG_OWN_REALTY')
plt.title('Income Totals per Family Status for Bottom Half of Earners')

# Rereate the Heatmap shown below
df = df.drop('FLAG_MOBIL', axis=1)
sns.heatmap(df.corr(), annot=False, fmt='.1g', cmap='coolwarm')

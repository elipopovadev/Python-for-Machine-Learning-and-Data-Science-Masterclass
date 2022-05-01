import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/eli/Desktop/application_record.csv')

# Rereate the Heatmap shown below
df = df.drop('FLAG_MOBIL', axis=1)
sns.heatmap(df.corr(), annot=False, fmt='.1g', cmap='coolwarm')

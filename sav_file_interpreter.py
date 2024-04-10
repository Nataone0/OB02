import pyreadstat
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

os.environ['LOKY_MAX_CPU_COUNT'] = '4'


# Replace 'path/to/your/file.sav' with the actual path to your SAV file
df, meta = pyreadstat.read_sav('D:\.marketing analytics\Sample1.sav')

# print(df.head())  # Prints the first five rows of the DataFrame for a preview
# print(df.columns)
# print(df.describe())
# 
# Histogram for 'no_units'
# sns.histplot(df['no_units'])
# plt.title('Distribution of Units Sold')
# plt.show()
#
# Histogram for 'sum_sale'
# sns.histplot(df['sum_sale'])
# plt.title('Distribution of Sales Amount')
# plt.show()
#
# Boxplot for 'no_units'
# sns.boxplot(x=df['no_units'])
# plt.title('Boxplot for Units Sold')
# plt.show()
#
# Boxplot for 'sum_sale'
# sns.boxplot(x=df['sum_sale'])
# plt.title('Boxplot for Sales Amount')
# plt.show()
#
# Count of sales by brands
# sns.countplot(y='BrandName', data=df, order = df['BrandName'].value_counts().index)
# plt.title('Sales Count by Brand')
# plt.show()
#
# Scatter plot for 'no_units' and 'sum_sale'
# sns.scatterplot(x='no_units', y='sum_sale', data=df)
# plt.title('Relationship Between Units Sold and Sales Amount')
# plt.show()
#
# Correlation matrix for quantitative variables
# corr = df[['no_units', 'sum_sale']].corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()


# Selecting features for clustering
features = df[['no_units', 'sum_sale']].dropna()

# Standardizing the features

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Performing KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # You can change the number of clusters
clusters = kmeans.fit_predict(features_scaled)

# Adding cluster labels to the original DataFrame
df['Cluster'] = np.nan
df.loc[features.index, 'Cluster'] = clusters

# Visualizing the clusters
sns.scatterplot(x='no_units', y='sum_sale', hue='Cluster', data=df, palette='viridis')
plt.title('Cluster Analysis of Units Sold vs Sales Amount')
plt.show()

# Convert 'txn_date' to datetime format
df['txn_date'] = pd.to_datetime(df['txn_date'])

# Aggregating sales amount over time (e.g., monthly)
monthly_sales = df.resample('ME', on='txn_date')['sum_sale'].sum()

# Plotting the time series
plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title('Monthly Sales Amount Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.show()

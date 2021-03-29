import pandas as pd
import numpy as np

df = pd.read_csv('salaries_by_college_major.csv')
#print(df.head())
#print(df.shape, "\n")
#print(df.columns)
#print(df.isna())
clean_df = df.dropna()
print(clean_df.tail())

print("******** Accessing Columns and Individual Cells in a dataframe********* ")
#print(clean_df['Starting Median Salary'])
#print(clean_df['Starting Median Salary'].max())
## Row number or index (major) that shows this much on average
# print(clean_df['Starting Median Salary'].idxmax())
#
# ## .loc[] gives the particular row (one way)
# print(clean_df['Undergraduate Major'].loc[43])
# ## second way
# print(clean_df['Undergraduate Major'][43])

## retrieving entire row, no column specified
#print(clean_df.loc[43])

print("****************** highest and lowest earning degrees ***********")
## highest mid career salary
# print("Highest mid career Sal:",clean_df['Mid-Career Median Salary'].max())
# print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
# print(clean_df['Undergraduate Major'][8])
#
# print("Lowest starting and Mid Career salary:", clean_df["Starting Median Salary"].min())
# print(clean_df["Undergraduate Major"].loc[clean_df['Starting Median Salary'].idxmin()])

print("****** Sorting Values and Adding Columns **********")
# ## Using literal subtraction sign
# print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df["Mid-Career 10th Percentile Salary"])
# ## Using subtraction method
# print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))
# ## Adding this to our existing dataframe with ,insert()
# spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df["Mid-Career 10th Percentile Salary"]
# clean_df.insert(1, "Spread", spread_col)
# print(clean_df.head())
#
# ## Sorting by lowest spread
# low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major', 'Spread']].head())
#
# ## DEGREES with highest potential
# highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
#
# ## Greatest spread
# highest_spread = clean_df.sort_values('Spread', ascending=False)
# print(highest_spread[['Undergraduate Major', 'Spread']].head())

print("********* Grouping and Pivoting DATA WITH PANDAS ****************")
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').count())
print(clean_df.groupby('Group').mean())


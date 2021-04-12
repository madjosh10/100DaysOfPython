import pandas as pd

df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# print(df)
print(df.head(5))
# last part of the dataset
print(df.tail())
# shape
print(df.shape)
#count
print(df.count())

# Groupby that has the TAG column and its rows. sum() to give the sum of each programming lang
print(df.groupby("TAG").sum())

# count() for entries per month
print(df.groupby("TAG").count())

# Data cleaning
print(type(df['DATE'][1]))

#Converting str to datetime objects
df.DATE = pd.to_datetime(df.DATE[1])
# print(df.to_datetime(df.DATE[1]))
print(df.head())

dif_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(dif_df)

dif_df.fillna(0, inplace=True)

# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)
#
# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)
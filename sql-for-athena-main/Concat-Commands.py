# default axis is 0 ( this stacks the Dataframes)
pd.concat([df1, df2])

# rest the index
pd.concat([df1, df2], ignore_index=True)

# can side by side by specifying axis=1
pd.concat([df1, df2], axis=1)

# default join is outer, but you can specify inner join
# there is no option for left or right joins
pd.concat([df1, df2], axis=1, join = 'inner')
pd.concat([df1, df2], axis=0, join = 'inner')

#Inner Join:
pd.merge(df1, df2, on = "col_name")

#Outer Join:
pd.merge(df1, df2, on = "col_name", how = "outer")

#Left Join:
pd.merge(df1, df2, on = "col_name", how = "left")

#Right Join:
pd.merge(df1, df2, on = "col_name", how = "right")

# option to add in for prefixes
suffixes = ["_l", "_r"]

# provide the type of join tot he table
indicator="indicator_col"
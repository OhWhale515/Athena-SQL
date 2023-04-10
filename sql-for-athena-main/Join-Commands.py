#Inner Join:
pd.merge(df1, df2, on = "col_name")

#Outer Join:
pd.merge(df1, df2, on = "col_name", how = "outer")

#Left Join:
pd.merge(df1, df2, on = "col_name", how = "left")

#Right Join:
pd.merge(df1, df2, on = "col_name", how = "right")
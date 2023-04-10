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

# Merge the two dataframes on loannumber
merged_df = pd.merge(preds_df, filter_df, on="loannumber", how="outer")

# Filter rows where loannumber is not in filter_df or prediction change > 10%
filtered_df = merged_df[~merged_df["loannumber"].isin(filter_df["loannumber"]) | (merged_df["prediction_change"] > 0.1)]

# Select only the relevant columns and output the rows
output_df = filtered_df[["loannumber", "prediction", "prediction_change"]]
print(output_df)

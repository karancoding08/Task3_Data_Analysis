import pandas as pd

print("===== TASK 3 DATA ANALYSIS =====")


df = pd.read_csv("sales_data.csv")

# Show full data
print("\nFULL DATA:")
print(df)


print("\nTOTAL SALES:", df["Sales"].sum())
print("AVERAGE SALES:", df["Sales"].mean())
print("MAX SALES:", df["Sales"].max())
print("MIN SALES:", df["Sales"].min())

print("\nCATEGORY WISE SALES:")
print(df.groupby("Category")["Sales"].sum())
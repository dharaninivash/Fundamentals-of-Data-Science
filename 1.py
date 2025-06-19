import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create the CSV
data = {
    "S.No.": [1,2,3,4,5,6,7,8,9,10],
    "NAME": ["Ajay", "Kumar", "Sara", "Zaira", "Sachin", "Rahul", "Pooja", "Smith", "Laxmi", "Michael"],
    "M1": [32, 58, 66, 34, 85, 90, 70, 85, 59, 81],
    "M2": [76, 81, 73, 62, 80, 86, 68, 90, 65, 69],
    "M3": [68, 72, 84, 64, 78, 83, 75, 92, 71, 74]
}
df = pd.DataFrame(data)
df.to_csv("marks.csv", index=False)

# Step 2: Read the data
df = pd.read_csv("marks.csv")
print("Full Data:\n", df)

# Step 3: First and last 5 rows
print("\nFirst 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())

# Step 4: Purpose of describe()
print("\nDescribe Function Output:\n", df.describe())
# Purpose: Gives count, mean, std, min, 25%, 50%, 75%, max of numeric columns

# Step 5: Select 3rd to 6th row
print("\n3rd to 6th rows:\n", df.iloc[2:6])

# Step 6: Select rows with M3 > 84
print("\nM3 > 84:\n", df[df["M3"] > 84])

# Step 7: Filter rows with missing values (example: add one for demo)
df.loc[2, 'M2'] = None  # add missing value temporarily
print("\nRows with missing values:\n", df[df.isnull().any(axis=1)])

# Step 8: Remove missing value rows
df_cleaned = df.dropna()
print("\nAfter removing missing value rows:\n", df_cleaned)

# Step 9: Sort M1 column descending
print("\nM1 sorted descending:\n", df.sort_values(by="M1", ascending=False))

# Step 10: Plot total marks
df["Total"] = df[["M1", "M2", "M3"]].sum(axis=1)
df.plot(x="NAME", y="Total", kind="bar", legend=False)
plt.title("Total Marks of Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# Step 11: Output for marks.ix[3:6, ['m2','m3']] using iloc
print("\nMarks from 3rd to 6th row (M2, M3):\n", df.iloc[3:7][["M2", "M3"]])

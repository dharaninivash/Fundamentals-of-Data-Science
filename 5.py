import pandas as pd

# Sample data
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 22]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Export to CSV
df.to_csv("people.csv", index=False)
print("Data exported to people.csv")

# Import (Read) from CSV
df_read = pd.read_csv("people.csv")
print("Imported DataFrame:")
print(df_read)

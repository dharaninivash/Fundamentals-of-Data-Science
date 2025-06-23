# Create a tuple
my_tuple = (100, 200, 300, 400, 500)
print("Original Tuple:", my_tuple)

# Slicing tuple
print("First 3 elements:", my_tuple[:3])
print("Last 2 elements:", my_tuple[-2:])

# Combining two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Combined Tuple:", combined_tuple)

# Matrix from two tuples
tuple_matrix = [tuple1, tuple2]
print("Tuple Matrix:")
for row in tuple_matrix:
    print(row)

# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Add elements from list2 to list1
list1.extend(list2)
print("Extended List:", list1)

# Create a matrix using list1 and list2
matrix = [list1[:3], list2]
print("Matrix:")
for row in matrix:
    print(row)

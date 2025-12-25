"""Basic array operations in Python using lists."""

# Create an array (list)
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

# Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Append an element
arr.append(6)
print("After append(6):", arr)

# Insert an element at a specific position
arr.insert(2, 10)
print("After insert(2, 10):", arr)

# Remove an element by value
arr.remove(3)
print("After remove(3):", arr)

# Remove an element by index
removed = arr.pop(1)
print("Popped element at index 1:", removed)
print("After pop(1):", arr)

# Get length
print("Length of array:", len(arr))

# Check if element exists
print("Is 4 in array?", 4 in arr)

# Sort the array
arr.sort()
print("After sort():", arr)

# Reverse the array
arr.reverse()
print("After reverse():", arr)

# Slice the array
sub_arr = arr[1:4]
print("Slice [1:4]:", sub_arr)
# Arrays in Python (DSA)

# Creating an array (list)
arr = [10, 20, 30, 40]

# Accessing elements
print(arr[0])
print(arr[2])

# Traversing array
for i in arr:
    print(i)

# Using index
for i in range(len(arr)):
    print(arr[i])

# Insertion
arr.append(50)
print(arr)

# Deletion
arr.pop()
print(arr)

# Update
arr[1] = 100
print(arr)

# Problem 1: Sum of elements
arr = [1, 2, 3, 4]
total = 0
for i in arr:
    total += i
print("Sum:", total)

# Problem 2: Maximum element
arr = [10, 50, 20, 40]
max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print("Max:", max_val)

# Problem 3: Count even numbers
arr = [1, 2, 3, 4, 6]
count = 0

for i in arr:
    if i % 2 == 0:
        count += 1

print("Even count:", count)

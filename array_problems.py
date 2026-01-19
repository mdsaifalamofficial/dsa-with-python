# Array Problems (Basic to Intermediate)

# 1. Traversal
arr = [10, 20, 30, 40]
for i in arr:
    print(i)

# 2. Reverse array (two pointer)
arr = [1, 2, 3, 4]
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed:", arr)

# 3. Linear Search
arr = [10, 20, 30, 40]
target = 30
found = False

for i in arr:
    if i == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")

# 4. Largest element
arr = [10, 50, 20, 40]
max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print("Max:", max_val)

# 5. Second largest
arr = [10, 50, 20, 40]
largest = second = -1

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)

# 6. Count even and odd
arr = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

# 7. Sum of elements
arr = [1, 2, 3, 4]
total = 0

for i in arr:
    total += i

print("Sum:", total)

# 8. Remove duplicates
arr = [1, 2, 2, 3, 4, 4]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print("Unique:", unique)

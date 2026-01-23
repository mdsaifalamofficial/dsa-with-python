# Linear Search Example

arr = [10, 20, 30, 40]
target = 30

found = False

for num in arr:
    if num == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")

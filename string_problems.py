# String Problems (DSA Practice)

# 1. String traversal
s = "python"
for ch in s:
    print(ch)

# 2. Reverse a string
s = "python"
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed:", rev)

# 3. Palindrome check
s = "madam"
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome")

# 4. Count vowels
s = "education"
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels:", count)

# 5. Character frequency
s = "banana"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Frequency:", freq)

# 6. Remove duplicate characters
s = "banana"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)

# 7. Count words
s = "I love python very much"
words = s.split()
print("Word count:", len(words))

# 8. String type checks
print("12345".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

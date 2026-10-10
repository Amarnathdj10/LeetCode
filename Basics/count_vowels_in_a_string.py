s = input("Enter a sentence: ")

count = 0
vowels = ['a','e','i','o','u']
for c in s:
    count += 1 if c.lower() in vowels else 0

print(count)
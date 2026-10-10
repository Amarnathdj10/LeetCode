# 2. Reverse a string without slicing

s = "hello"

word = list(s)

i = 0
j = len(s)-1

while i < j:

    word[i], word[j] = word[j], word[i]
    i += 1
    j -= 1

print(("".join(word)))
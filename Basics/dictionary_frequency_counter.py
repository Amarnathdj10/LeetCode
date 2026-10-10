s = input("Enter word/sentence: ")

hashmap = {}

for c in s.lower():
    hashmap[c] = hashmap.get(c,0) + 1

print(hashmap)
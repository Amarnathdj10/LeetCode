matrix = [[1, 2], [3, 4], [5]]
answer = []

for item in matrix:
    if isinstance(item,list):
        answer.extend(item)
    else:
        answer.append(item)

print(answer)
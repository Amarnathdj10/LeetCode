#List comprehension: squares of even numbers up to N

n = int(input("Enter number: "))
squares = [i**2 for i in range(2,n+1) if i % 2 == 0]
print(squares)
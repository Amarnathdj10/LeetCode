def fact(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * fact(n-1)

n = int(input("Enter a number: "))

factorial = fact(n)
print(factorial)
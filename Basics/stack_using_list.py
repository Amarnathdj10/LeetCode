stack = []

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            value = int(input("Enter number to push: "))
            stack.append(value)

        case 2:
            if stack: 
                value = stack.pop()
                print("Popped elemeent: ",value)
            else:
                print("Stack is empty")

        case 3:
            if stack:
                print("Top element: ",stack[-1])
            else:
                print("Stack is empty")

        case 4:
            if not stack:
                print("Stack is empty")

        case 5:
            break

        case _:
            print("Invalid choice")

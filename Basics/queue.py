from collections import deque

queue = deque()

while True:

    print("1) Enqueue")
    print("2) Dequeue")
    print("3) Peek front")
    print("4) Peek rear")
    print("5) Check empty")
    print("6) Exit")

    choice = int(input("\nEnter user choice: "))

    match choice:

        case 1:
            x = int(input("Enter element to enqueue: "))
            queue.append(x)

            print("Current queue: ",queue)

        case 2:
            removed = queue.popleft()
            print("Dequeued value: ",removed)

            print("Current queue: ",queue)

        case 3:
            print("Front: ",queue[0])

        case 4:
            print("Rear: ",queue[-1])

        case 5:
            print("Empty: ",len(queue)==0)

        case 6:
            exit(0)

        case 7:
            break

        case _:
            print("Invalid choice")

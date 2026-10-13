class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete(self,value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        print("Value not found")


    def print_list(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end = " -> ")
            current = current.next

        print("None")


l1 = SinglyLinkedList()

l1.insert_head(20)
l1.insert_head(10)
l1.insert_tail(30)
l1.insert_tail(40)

l1.print_list()

l1.delete(20)
l1.print_list()





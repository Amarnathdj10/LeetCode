'''
In Pen-Paper coding round the question is based on Linked List + Hash Map.
You have to write 3 functions.

The Linked List Node contains:
lockId - integer
keyId - integer
next pointer

Functions to Implement
1. Map lockId with keyId and store the mapping inside Hash Map
2. Traverse the Linked List and print the data
3. Sort the Linked List based on keyId
'''

class Node:

    def __init__(self, lockId, keyId):

        self.lockId = lockId
        self.keyId = keyId
        self.next = None

    def map_lock_to_key(head):

        hashmap = {}
        curr = head

        while curr:

            hashmap[curr.lockID] = curr.keyId
            curr = curr.next

        return hashmap

    def print_list(head):

        curr = head

        while curr:

            print(f"[Lock: {curr.lockId}, Key: {curr.keyId}] -> ", end = " ")
            curr = curr.next

        print("None")

    def mergeSort(head):

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = mergeSort(head)
        right = mergeSort(mid)

        return merge(left, mid)

    def merge(l1, l2):

        dummy = Node(0, 0)
        temp = dummy

        while l1 and l2:

            if l1.keyId <= l2.keyId:
                temp.next = l1
                l1 = l1.next

            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        temp.next = l1 if l1 else l2

        return dummy.next
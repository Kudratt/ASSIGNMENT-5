class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_and_delete(head, key):
    count = 0
    dummy = Node(0)
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if curr.data == key:
            count += 1
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next, count


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(1)

key = 1
head, cnt = count_and_delete(head, key)
print("Count:", cnt)

# Print updated list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("NULL")

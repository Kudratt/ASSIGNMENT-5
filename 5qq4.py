class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original: 1->2->3->4->NULL")
head = reverse_list(head)

# Print reversed
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("NULL")

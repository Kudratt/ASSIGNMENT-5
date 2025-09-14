class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_before(self, key, data):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == key:
            self.insert_begin(data)
            return
        prev, curr = None, self.head
        while curr and curr.data != key:
            prev, curr = curr, curr.next
        if curr:
            new_node = Node(data)
            prev.next = new_node
            new_node.next = curr
        else:
            print("Key not found")

    def insert_after(self, key, data):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Key not found")

    def delete_begin(self):
        if not self.head:
            print("List empty")
            return
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            print("List empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_node(self, key):
        if not self.head:
            print("List empty")
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        prev, curr = None, self.head
        while curr and curr.data != key:
            prev, curr = curr, curr.next
        if curr:
            prev.next = curr.next
        else:
            print("Node not found")

    def search(self, key):
        pos, temp = 1, self.head
        while temp:
            if temp.data == key:
                print(f"Node {key} found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print("Node not found")

    def display(self):
        if not self.head:
            print("List empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# Menu-driven
sll = SinglyLinkedList()
while True:
    print("\n1.InsertBegin 2.InsertEnd 3.InsertBefore 4.InsertAfter")
    print("5.DeleteBegin 6.DeleteEnd 7.DeleteNode 8.Search 9.Display 10.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        val = int(input("Enter value: "))
        sll.insert_begin(val)
    elif ch == 2:
        val = int(input("Enter value: "))
        sll.insert_end(val)
    elif ch == 3:
        key = int(input("Enter key: "))
        val = int(input("Enter new value: "))
        sll.insert_before(key, val)
    elif ch == 4:
        key = int(input("Enter key: "))
        val = int(input("Enter new value: "))
        sll.insert_after(key, val)
    elif ch == 5:
        sll.delete_begin()
    elif ch == 6:
        sll.delete_end()
    elif ch == 7:
        key = int(input("Enter node to delete: "))
        sll.delete_node(key)
    elif ch == 8:
        key = int(input("Enter value to search: "))
        sll.search(key)
    elif ch == 9:
        sll.display()
    else:
        break

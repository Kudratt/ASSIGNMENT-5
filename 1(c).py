    def insert_before(self, key, data):
        if not self.head:
            print("List empty")
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

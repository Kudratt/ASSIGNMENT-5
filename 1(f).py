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

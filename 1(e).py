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

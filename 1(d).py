    def delete_begin(self):
        if not self.head:
            print("List empty")
            return
        self.head = self.head.next

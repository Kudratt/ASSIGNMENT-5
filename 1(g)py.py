    def search(self, key):
        pos, temp = 1, self.head
        while temp:
            if temp.data == key:
                print(f"Node {key} found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print("Node not found")

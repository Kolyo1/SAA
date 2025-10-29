class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                return True
            
            curr = curr.next
        return False
    
    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def forward(self):
        curr = self.head
        print("\nForward")
        while curr:
            print(curr.data, end=" <-> " if curr.next else "\n")
            curr = curr.next 

    def backwards(self):
        curr = self.tail
        print("\nBackwards")
        while curr:
            print(curr.data, end=" <-> " if curr.prev else "\n")
            curr = curr.prev

dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.forward()
dll.backwards()

print("\nSearching for element 20 : ", "Found" if dll.search(20) else "Not Found")
print("\nSearching for element 50 : ", "Found" if dll.search(50) else "Not Found")

print("\nRemoving element 20 : ", "Removed" if dll.remove(20) else "Not Found")
dll.forward()
dll.backwards()

print("\nRemoving element 50 : ", "Removed" if dll.remove(50) else "Not Found")
dll.forward()
dll.backwards()
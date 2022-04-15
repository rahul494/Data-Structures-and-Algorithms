class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next

    def add_first(self, node):
        if self.head:
            node.next = self.head
        self.head = node
    
    def add_last(self, node):
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = node


ll = LinkedList(Node(1))
ll.add_first(Node(2))
ll.add_first(Node(3))
ll.add_last(Node(0))
ll.print()
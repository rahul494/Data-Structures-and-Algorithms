class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_first(self, node):
        if self.head:
            node.next = self.head
        self.head = node

    def print(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse_list(self):
        prev = None
        while self.head:
            temp = self.head
            self.head = self.head.next 




ll = LinkedList(Node(5))
ll.add_first(Node(4))
ll.add_first(Node(3))
ll.add_first(Node(2))
ll.add_first(Node(1))
ll.print()
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse(root):
    prev, head, temp = None, root, None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = reverse(head)
result.print_list()
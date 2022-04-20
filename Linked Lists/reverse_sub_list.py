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

def reverse_sub_list(head, p, q):
    if p == q:
        return head
    
    curr, prev = head, None
    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1
        
    last_node_of_first_part = prev
    last_node_of_sub_list = curr

    next = None
    i = 0

    while curr and i < q - p + 1:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        i += 1

    # connect with first part
    if last_node_of_first_part:
        last_node_of_first_part.next = prev
    else:
        head = prev
    
    last_node_of_sub_list.next = curr

    return head



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

result = reverse_sub_list(head, 2, 5)
result.print_list()
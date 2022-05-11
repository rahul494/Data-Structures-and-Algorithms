class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_middle(head):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.value

    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList middle is " + str(list_middle(head)))

    head.next.next.next.next.next.next = Node(7)
    print("LinkedList middle is " + str(list_middle(head)))

    head.next.next.next.next.next.next.next = Node(8)
    print("LinkedList middle is " + str(list_middle(head)))
    
    head.next = None
    print("LinkedList middle is " + str(list_middle(head)))
    
    head.next = Node(2)
    print("LinkedList middle is " + str(list_middle(head)))
    
    head.next.next = Node(3)
    print("LinkedList middle is " + str(list_middle(head)))
    
main()
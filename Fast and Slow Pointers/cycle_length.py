class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            curr_node = slow.next
            curr_length = 1

            while curr_node != slow:
                curr_node = curr_node.next
                curr_length += 1

            return curr_length
    
    return 0

    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle of length " + str(cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle of length " + str(cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle of length " + str(cycle_length(head)))

    head.next = head
    print("LinkedList has cycle of length " + str(cycle_length(head)))

main()
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True

    slow, fast = head, head
    prev, temp = None, None

    # reverse first half of linked list
    while fast and fast.next:
        fast = fast.next.next
        # change pointer to previous node
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        
    while temp and prev and temp.next and prev.next:
        if temp.value != prev.value:
            return False

        temp = temp.next
        prev = prev.next
    
    if temp.value == prev.value and not temp.next and not prev.next:
        return True
    else:
        return False
    
def print_list(head):
    curr = head
    while curr:
        print(curr.value, end=" ")
        curr = curr.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Is LinkedList a palindrome? " + str(is_palindrome(head)))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    print("Is LinkedList a palindrome? " + str(is_palindrome(head)))
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next = Node(7)
    print("Is LinkedList a palindrome? " + str(is_palindrome(head)))

    head = Node(1)
    print("Is LinkedList a palindrome? " + str(is_palindrome(head)))

    head = None
    print("Is LinkedList a palindrome? " + str(is_palindrome(head)))

main()
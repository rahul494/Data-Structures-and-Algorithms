def reverse_iterative(self):
    prev = None
    cur = self.head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    
    self.head = prev
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        headA_pointer = headA
        headB_pointer = headB
        
        if headA_pointer is None or headB_pointer is None:
            return None
        
        while headA_pointer != headB_pointer:
            if headA_pointer is None:
                headA_pointer = headB
            else:
                headA_pointer = headA_pointer.next
            
            if headB_pointer is None:
                headB_pointer = headA
            else:
                headB_pointer = headB_pointer.next
                
        return headA_pointer

    
    def print(self, node):
        while node:
            print(node.val)
            node = node.next


s = Solution()

# listA = [4,1,8,4,5]
node_a_4 = ListNode(5)
node_a_3 = ListNode(4, node_a_4)
node_a_2 = ListNode(8, node_a_3)
node_a_1 = ListNode(1, node_a_2)
node_a_0 = ListNode(4, node_a_1)

# listB = [5,6,1,8,4,5]
node_b_5 = ListNode(5)
node_b_4 = ListNode(4, node_b_5)
node_b_3 = ListNode(8, node_b_4)
node_b_2 = ListNode(1, node_b_3)
node_b_1 = ListNode(6, node_b_2)
node_b_0 = ListNode(5, node_b_1)

print(s.print(node_b_0))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = l1
        carry = 0

        while l1 or l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            l1.val = sum % 10
            l1 = l1.next
            l2 = l2.next

        return head



    def print(self, node):
        while node:
            print(node.val)
            node = node.next


s = Solution()
n1 = ListNode(3)
n2 = ListNode(4, n1)
n3 = ListNode(2, n2)

n4 = ListNode(4)
n5 = ListNode(6, n4)
n6 = ListNode(5, n5)

resu = s.addTwoNumbers(n3, n6)
s.print(resu)
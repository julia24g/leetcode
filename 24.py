# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        
        a = head
        
        if head is None or head.next is None:
            return head
        else:
            b = a.next
            while b != None:
                a.next = self.swapPairs(b.next)
                b.next = a
                return b

# create test linked list 1 -> 2 -> 3 -> 4
node = head = ListNode(1)
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)

sol = Solution()
head = sol.swapPairs(head)

print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)

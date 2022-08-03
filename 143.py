# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        #reverse second half of list
        prev = slow
        curr = prev.next
        prev.next = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
            
        l1 = head
        l2 = prev
        
        while l2.next:
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp
            
            l1 = temp
            l2 = temp2
        
        head = l1

# create test linked list 1 -> 2 -> 3 -> 4
node = head = ListNode(1)
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)

s = Solution()
s.reorderList(head)
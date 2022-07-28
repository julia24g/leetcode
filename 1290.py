# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count = 0
        current = head[0]
        
        while current.next != None:
            count += 1
            current = current.next
            
        decimal = 0
        current = head[0]
        
        for x in range(count + 1):
            decimal += 2^(count - x) * current.val
            current = current.next
        
        return decimal

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

newList = ListNode(1, 0)
for x in range(4):
    newList.next = 1
    newList
    current = current.next

print(newList)

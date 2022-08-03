#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        s = ListNode(0)
        arr = [0]*lists

        for x in range(lists):
            arr[x] = lists[x]
        
        sorted_arr = sorted(arr)

        current = s
        while not sorted_arr[0]:
            smallest = sorted_arr[0]
            n = ListNode(smallest)
            current.next = n
            current = current.next
            smallest = smallest.next
            sorted_arr[0] = smallest
            sorted_arr = sorted(sorted_arr)

        
        return s.next

class createListNode:
    def create(self, )


class Test:

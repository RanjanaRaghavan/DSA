# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        hare = head
        tortoise = head

        #Find Mid point
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        
        #Reverse second half
        curr = tortoise
        prev = None

        while curr:
            curr.next ,prev,curr = prev,curr,curr.next
        
        #Find max of twin
        max_val = 0

        start = head

        while prev:

            max_val = max(max_val, prev.val + start.val)
            prev = prev.next
            start = start.next

        return max_val 
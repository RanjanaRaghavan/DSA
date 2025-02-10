# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        #declare a linked list in python
        dummyHead = ListNode(0)
        curr = dummyHead

        carry = 0
        
        while l1 != None  or l2 != None or carry!= 0:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1+val2 + carry
            carry = sum //10
            new_node = ListNode(sum % 10)

            curr.next = new_node #--> This is to connect the dummy head to the node
            curr = new_node #this is to adjust the position of curr to this node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyHead.next




        
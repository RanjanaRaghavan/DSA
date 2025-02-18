"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        Q = collections.deque([root])
        
        while Q:

            cur_size = len(Q)

            for i in range(cur_size):

                node = Q.popleft()

                if i < cur_size -1:
                    node.next = Q[0]
            
                if node.left:
                    Q.append(node.left)
                
                if node.right:
                    Q.append(node.right)
        
        return root

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        Q = collections.deque([root])
        res = []
        cur_size = len(Q)

        while Q:

            for i in range(cur_size):

                node = Q.popleft()
                if i == cur_size -1:
                    res.append(node.val)

                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)
            
            cur_size = len(Q)
        
        return res
                


        
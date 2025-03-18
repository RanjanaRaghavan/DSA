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

        while Q:

            cursize = len(Q)

            for i in range(cursize):

                node = Q.popleft()

                if i == cursize -1:
                    res.append(node.val)
                
                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)
            
        return res

        
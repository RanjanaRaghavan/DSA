# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        #leaf - complete tree , if no left then no right too
        if not root.left :
            return 1
        
        left_count = self.countNodes(root.left) if root.left else 0
        right_count = self.countNodes(root.right) if root.right else 0


        return 1 + left_count + right_count
        

        
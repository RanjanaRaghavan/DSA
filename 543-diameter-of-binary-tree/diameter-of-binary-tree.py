# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def depthOftree(root):

            if root is None:
                return 0

            leftdepth = depthOftree(root.left)
            righdepth = depthOftree(root.right)

            self.diameter = max(self.diameter, (leftdepth + righdepth))

            return max(righdepth ,leftdepth) +1

        depthOftree(root)
        return self.diameter
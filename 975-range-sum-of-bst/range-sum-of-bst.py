# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            sum = 0
            if not node:
                return 0
            
            if low <= node.val <= high:
                sum += node.val

            left = dfs(node.left)
            right = dfs(node.right)

            return sum + left + right
        
        return dfs(root)
    


        
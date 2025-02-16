# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        arr = []

        def dfs(node):
            if node is None:
                return 
            
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(arr)
        arr.sort()

        minval = float('inf')  

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < minval:
                minval = diff

        return minval

        
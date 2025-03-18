# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        one = []
        two = []

        one = self.dfs(root1,one)
        two = self.dfs(root2,two)

        print(one,two)
        return one == two

    
    def dfs(self,node,arr):

        if node is None:
            return arr
        
        if node.left is None and node.right is None:
            arr.append(node.val)
        
        if node.left:
            self.dfs(node.left,arr)
        
        if node.right:
            self.dfs(node.right,arr)
        
        return arr
        


        
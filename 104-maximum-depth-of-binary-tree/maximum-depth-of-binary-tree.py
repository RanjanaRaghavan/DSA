# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxCount = [0]
        cur_count = 0
        self.dfs(root,maxCount,cur_count)

        return maxCount[0]


    
    def dfs(self,node,maxCount,cur_Count):

        if node is None:
            return None
        
        cur_Count +=1

        #Leaf Node
        if node.right is None and node.left is None:
            maxCount[0] = max(maxCount[0], cur_Count)
        
        #Non Leaf
        if node.left:
            self.dfs(node.left,maxCount,cur_Count)
        
        if node.right:
            self.dfs(node.right,maxCount,cur_Count)

        
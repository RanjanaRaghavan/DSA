# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
            Helper - Our function needs to return 2 things
            1. Am i balanced
            2. What is my height?
            So return (status, height)

            Every subtree returns this, and then we can bubble up to root
        '''

        def dfs(node):

            if not node:
                return (True, 0)
            
            left_status, left_height = dfs(node.left)
            right_status, right_height = dfs(node.right)

            height = 1 + max(left_height, right_height)

            status = left_status and right_status and abs(left_height - right_height) <=1
            
            return status,height
            
        return dfs(root)[0]



        

        


        
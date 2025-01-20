# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        '''
        Process children first and then go come to parent
        1. 1 list to have the path
        2. Call helper function 
        3. Return the list
        '''
        path = []
        self.dfs(root,path)
        return path



    #Helper Function
    '''
    Input 
    1. root
    2. list
    Do : Append to list
    '''
    def dfs(self,root,path):

        #None check
        if root is None:
            return None

        #leaf node check
        if root.left is None and root.right is None:
            path.append(root.val)
            return

        #none leaf node check
        if root.left:
            self.dfs(root.left,path)
        
        if root.right:
            self.dfs(root.right, path)
        
        #Append to path only after 
        path.append(root.val)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        '''
            Process yourself then go to children
            1. List that we will return
            2. Call helper function
            3. Return list

        '''
        path = []
        self.dfs(root,path)

        return path
        


    '''
        Helper function
        Inputs :
        1.root
        2.list
    '''
    def dfs(self,root,path):

        #None check
        if root is None:
            return None
        
        path.append(root.val)

        #leaf Node check
        if root.left is None and root.right is None:
            return

        #not a leaf node check
        
        if root.left:
            self.dfs(root.left,path)
        
        if root.right:
            self.dfs(root.right,path)
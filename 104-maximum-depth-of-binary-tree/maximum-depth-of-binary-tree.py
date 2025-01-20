# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        1. maxcount to keep track of maxCount
        2. current count 
        3. Helper Function call
        4. return maxcount 
        '''

        max_count = [0]
        cur_count = 0
        self.dfs(root,cur_count,max_count)
        
        return max_count[0]
    
    '''
    Pre order traversal
    Helper Function
    Input
    1. root
    2.cur count
    3 max count

    Do: Calculate cur count
        Calculate MaxCount
    '''
    def dfs(self,root,cur_count,max_count):

        #None check
        if root is None:
            return None

        #increase count
        cur_count += 1

        #Leaf node check (check for maxCount)
        if root.left is None and root.right is None:
            max_count[0] = max(max_count[0],cur_count)

        #Non leaf node 
        if root.left:
            self.dfs(root.left,cur_count,max_count)
        
        if root.right:
            self.dfs(root.right,cur_count,max_count)
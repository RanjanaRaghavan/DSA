# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        1. Have a list for paths you want to return that
        2. Have a string cur_String which helps form that path eg 1->2->5
        3. Helper function to construct that string and append in array
        '''
        paths = []
        cur_string = ''
        #Helper function call
        self.dfs(root,cur_string,paths)
        return paths

    def dfs(self,root,cur_string,paths):

        #Check base condition
        if root is None:
            return None
        
        #Leaf node check
        if root.left is None and root.right is None:
            cur_string += str(root.val)
            paths.append(cur_string)
            return

        #Not a leaf Node check
        if root.left:
            self.dfs(root.left, cur_string + str(root.val) + '->',paths)

        if root.right:
            self.dfs(root.right, cur_string + str(root.val) + '->',paths)
        
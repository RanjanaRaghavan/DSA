# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        #Base Case
        if root is None:
            return []
        
        path = []
        dq = collections.deque([root])

        while(len(dq) > 0):

            #For level tracking
            cur_level = len(dq)
            level = []

            while cur_level > 0:
                
                cur_node = dq.popleft()
                
                #First go to children
                if cur_node.left:
                    dq.append(cur_node.left)
                
                if cur_node.right:
                    dq.append(cur_node.right)

                #then append to level
                level.append(cur_node.val)
                cur_level -=1
            
            path.append(level)
        
        return path[::-1]

        


        
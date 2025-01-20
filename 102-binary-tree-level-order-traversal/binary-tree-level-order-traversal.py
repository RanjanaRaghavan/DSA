# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            BFS
            1. Have a path output list
            2. Have a DQ to get the items in current level
            3.While DQ exists
            4. Have a currlevel check and level list to keep track
            5. Update path after every level
            6. Return path 
        '''

        #Base Case
        if root is None:
            return []

        path = []
        dq = collections.deque([root])

        while(len(dq) > 0):
            
            #to keep track of level
            cur_level = len(dq)
            level = []
            
            while(cur_level > 0 ):

                #Append node to level
                cur_node = dq.popleft()
                level.append(cur_node.val)

                #Add children node back in DQ
                if cur_node.left:
                    dq.append(cur_node.left)
                
                if cur_node.right:
                    dq.append(cur_node.right)

                cur_level -=1
        
            path.append(level)

        return path


        
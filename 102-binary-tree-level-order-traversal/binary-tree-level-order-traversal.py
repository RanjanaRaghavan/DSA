# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
            1. list path
            2. BFS
            3. return path
        '''

        '''
        1. dq = collections.deque([root])
        2. while dq exists
            get current node dq.popleft()
            add its left and right in -> dq.append()
        '''

        #none check
        if root is None:
            return []
        
        path = []
        dq = collections.deque([root])

        while(len(dq) > 0):

            cur_level = len(dq)
            level = []

            while cur_level >0:

                cur_node = dq.popleft()
                level.append(cur_node.val)

                if cur_node.left:
                    dq.append(cur_node.left)
                
                if cur_node.right:
                    dq.append(cur_node.right)

                cur_level -=1
            
            path.append(level)


        return path
        
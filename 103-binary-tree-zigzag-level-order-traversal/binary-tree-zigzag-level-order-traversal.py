# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        path = []

        if root is None:
            return path
        

        dq = collections.deque([root])

        while len(dq) > 0:
            cur_level =len(dq)
            level = []

            while cur_level > 0:

                cur_node = dq.popleft()
                level.append(cur_node.val)

                if cur_node.left:
                    dq.append(cur_node.left)

                if cur_node.right:
                    dq.append(cur_node.right)
                
                cur_level -=1
            
            path.append(level)
        
        #Manipulate the path list
        flag = False
        for i in range(len(path)):
            if flag == True:
                path[i] = path[i][::-1]
                flag = False
            else:
                flag = True

        return path




        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        Q = collections.deque([root])
        max_sum = float("-inf")
        level = 0
        max_level =0

        while Q:
            sum = 0
            level +=1
            cur_level_size = len(Q)
            for i in range(cur_level_size):

                node = Q.popleft()
                sum += node.val

                if node.left:
                    Q.append(node.left)
                
                if node.right:
                    Q.append(node.right)
            
            if sum > max_sum:
                max_sum = sum
                max_level = level
        
        return max_level
        
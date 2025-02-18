# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        Q = collections.deque([root])
        arr = []

        while Q:

            cur_level = []
            cur_size = len(Q)

            for _ in range(cur_size):

                node = Q.popleft()
                cur_level.append(node.val)

                if node.left:
                    Q.append(node.left)

                if node.right:
                    Q.append(node.right)

            arr.append(cur_level)

        return arr[::-1]        
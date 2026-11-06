# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find our path, we will tak current node, if we have children we'll use that path
        # and compare to max of left and right
        big = root.val  # default to root value for now


        def dfs(node):
            if not node: return None
            current = node.val
            left = dfs(node.left)
            left = left if left is not None else 0
            right = dfs(node.right)
            right = right if right is not None else 0

            # check if we are max
            nonlocal big
            big = max(big, current+left+right)
            
            return max(current, current+left, current+right)



        
        dfs(root)


        return big
        
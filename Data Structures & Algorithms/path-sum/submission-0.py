# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # we need to iteratively search down to see if we can find a sum equal to the values
        if not root: return False

        queue = [(0, root)]

        while queue: 
            count, node = queue.pop()

            # this is a child case
            if not node.left and not node.right: 
                if (node.val+count == targetSum):
                    return True
            else:
                if node.left:
                    queue.append((node.val+count,node.left))
                if node.right:
                    queue.append((node.val+count,node.right))
            

        return False
        
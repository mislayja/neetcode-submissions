# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #I've done this problem before
        # we need to check to verify l < curr < right
        # and also track the max at each step
        

        def isValid(node, max_val, min_val):
            if not node: return True
            if node.val >= max_val or node.val <= min_val:
                return False
            # we need to check children here
            if node.left:
                # if we're going left, we want to update new max with current value
                if not isValid(node.left, node.val, min_val): return False
            if node.right:
                if not isValid(node.right, max_val, node.val): return False
            return True

        return isValid(root,1000000001, -1000000001 )
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None, max_val=float('inf'), min_val=float('-inf')) -> bool:
        # we can recurse down verifying the right > left ...
        # lets worry about tracking bounds when we need to do that. 
        # if not root: return True

        # if root.left and root.left.val >= root.val: return False
        # if root.right and root.right.val <= root.val: return False
        
        # if not self.isValidBST(root.left) or not self.isValidBST(root.right): return False
        # return True

        # ok we need to account for bounds now :)

        # we can track at call site the max/min and return false if it's greater than/less than those fields. 
        if not root: return True
        # if we see same values, it's bad, strictly greater/less than allowed. 
        if root.val>=max_val or root.val <= min_val: return False

        # we can skip this because, our min/max check will verify this for us already.
        # if root.left and root.left.val >= root.val: return False
        # if root.right and root.right.val <= root.val: return False

        new_max = min(max_val, root.val)
        new_min = max(min_val, root.val)
        if not self.isValidBST(root.left, new_max, min_val) or \
           not self.isValidBST(root.right, max_val, new_min): return False
        return True
        

        
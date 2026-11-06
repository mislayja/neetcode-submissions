# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # we can call this recursively :)
        # check children, then evaluate self
        # let's assume we wont ever call null
        match(root.val):
            case 1: return True
            case 0: return False
            case 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            case 3: 
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
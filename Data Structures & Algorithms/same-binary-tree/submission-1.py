# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(f"p={p}, q={q}, false ret={not q or not p}, true ret={not q and not q}")
        if not q and not p: 
            return True
        elif not q or not p:
            return False
        
        if p.val != q.val:
            return False
        
        return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
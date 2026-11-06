# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # all node.val's are unique, thats good to see
        # p and q qill be in tree:)
        if not root: return None

        # if we ourselves are the node, we dont really care whats under us as we'll just return ourselves anywas
        # we're either the edge case were they are under, in which case we already are the ansewer
        # or we're the case where it's above us, in which case the conditions below will handle it :)
        # if root.val == p.val or root.val == q.val:
        #     return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right: return root
        # if left: return left
        # else: return right
            
        # forgot this is bst, this simplifies solution
        if root.val == p.val \
        or root.val == q.val \
        or (root.val<p.val and root.val>q.val) \
        or (root.val<q.val and root.val>p.val):
            return root
        if root.val > p.val and root.val > q.val:
            # bigger than both move left
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
            return self.lowestCommonAncestor(root.right, p, q)

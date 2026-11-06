# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None, isSubtreeCheck=False) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        
        # ok we see if root is equal to subroot
        # if so we need to check the subc
        # print(f"root:{root.val}, subRoot:{root.val}, isSubtreeCheck:{isSubtreeCheck}")

        if isSubtreeCheck:
            # only way to return true is for values to be equal and look at subequent
            if root.val == subRoot.val and self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True): 
                return True
            return False
        if root.val == subRoot.val:
            validSubtree = self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)
            if validSubtree: return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

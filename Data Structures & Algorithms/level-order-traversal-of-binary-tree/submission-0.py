# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # idea is iterative bfs.  at each layer we add our current node to res, and queue up children 

        res = []
        l = []
        if root:
            l.append(root)
        while l:
            res_l = []
            temp = []
            for item in l:
                res_l.append(item.val)
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            res.append(res_l)

            l = temp


        return res
        
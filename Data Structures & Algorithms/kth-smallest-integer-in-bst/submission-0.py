# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # need to look left and acctp that None could be a return value...
        # if have no children in left, then we look right as needed :)
        # need to look left and get a number from left that says # of tiles in left and then do same for right...

        # we want dfs here prioritizing left side
        # lets have left be the number of nodes found, and right be the result
        def search(node, k) -> (int, int):
            if not node: return (0, None)

            #look left
            left_nodes, ans = search(node.left, k)
            # print(f"Node:{node.val}, with left_nodes={left_nodes}, ans={ans}, k={k}")
            if ans is not None: return (0, ans)
            if left_nodes == k-1: return (0, node.val)
            right_nodes, ans = search(node.right, k-left_nodes-1)
            # print(f"Node:{node.val}, with right_nodes={right_nodes}, ans={ans}, k={k}")
            if ans is not None: return (0, ans)
            return ((left_nodes + right_nodes+1), None)


            # takeaways, I need to get better at update input params, explicitily using None check for invalid values, and seeing off by 1 errors sooner. 



        _, res = search(root, k)
        return res        
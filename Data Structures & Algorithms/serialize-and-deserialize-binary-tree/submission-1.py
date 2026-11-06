# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         res = ""
#         def dfs(node):
#             nonlocal res
#             if not node: 
#                 res+="N "
#                 return 
#             res+= str(node.val)+" "
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)
#         # print(res)
#         return res
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         data = data.split()
#         # print(data)
#         # lets just use recursion + return values        
#         def dfs(start_idx): # (TreeNode, int)
#             nonlocal data
#             if data[start_idx] == 'N': return (None, 1)
#             node = TreeNode(val=int(data[start_idx]))
#             node.left, num_used_l = dfs(start_idx+1)
#             node.right, num_used_r = dfs(start_idx+1+num_used_l)
#             return (node, 1+num_used_l+num_used_r)
        
#         head, _ = dfs(0)



#         return head
        
#         # while stack:
            

        

# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
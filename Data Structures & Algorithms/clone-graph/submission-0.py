"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # lets solve this iterately and not recursive
        if not node: return None
        

        clones = {node: Node(node.val)}
        queue = [node]

        while queue:
            orig = queue.pop()
            for child in orig.neighbors:
                # want to check if this child is in clones, if so skip
                if child not in clones:
                    # new node here, we want to create a node and add original to the queue
                    clones[child] = Node(child.val)
                    queue.append(child)
                # need to add to children of current node now
                clones[orig].neighbors.append(clones[child])
            


        return clones[node]
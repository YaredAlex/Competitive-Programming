from typing import Optional 
"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def solution(node:Optional['Node']):
    seen = {}
    # create a dfs method to traverse node in to deep for copy every element
    def dfs(tmp_node):
        if len(node.neighbor)==0:
            return Node(node.val)
        # make a copy node
        copy_node = Node(node.val,[])
        # keep track of copy Node based on node val since every node have unique val
        seen[node.val] = copy_node
        for neighbor in tmp_node.neighbors:
            if neighbor.val in seen:
                copy_node.append(seen[neighbor.val])
            else:
                copy_node.append(dfs(neighbor))

        return copy_node
    
    if node==None:
        return None
    return dfs(node)
    
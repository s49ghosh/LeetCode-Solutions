"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    # Do BFS from start node, as we explore make clones and store in hashmap, hashed on node val
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        
        queue = deque()

        # Start with given node
        queue.append(node)
        clones = {node.val: Node(node.val, [])}

        # BFS
        while queue:
            curr = queue.popleft()
            clone = clones[curr.val]

            # Iterate thru each of curr's neighbors
            for neighbor in curr.neighbors:

                # If we haven't cloned the neighbor yet
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                
                # Add cloned neighbor to current clone's neighbor list
                clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
        
            
        
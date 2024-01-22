class Solution:

    # Create a graph representation and a list of leaves. 
    #   While there are at least 2 nodes left prune leaves 
    #   At the end, we will be left with nodes to root our tree
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1 Node, return right away
        if n == 1: return [0]
        graph = defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
        # Leaves are edges with only one neighbor, to its parent
        leaves = [edge for edge in graph.keys() if len(graph[edge]) == 1]
        
        # If n > 2, we can perform pruning
        while n > 2:
            # We will prune len(leaves) nodes
            n -= len(leaves)
            nextLeaves = []

            # Iterate through leaves to do pruning. For each leaf, remove it from its neighbor's adjList
            for leaf in leaves:
                neigh = graph[leaf].pop()
                graph[neigh].remove(leaf)

                # If the neighbor now only has one neighbor, it is a leaf, add it to next iteration's leaves
                if len(graph[neigh]) == 1:
                    nextLeaves.append(neigh)
                # Remove leaf from the graph    
                del graph[leaf]
            
            # Update leaves to next iteration's leaves
            leaves = nextLeaves

        # The nodes left are our root(s)
        return list(graph.keys())

            
            
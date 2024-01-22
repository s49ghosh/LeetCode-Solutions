class LRUNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # Use a hashmap to achieve O(1) lookup times for a node given a value
    #   Use a doubly linked list to achieve efficient removal of LRU node
    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        # Dummy nodes to simplify insert and remove. The real nodes lie between these dummy nodes
        self.front = LRUNode(0, 0)
        self.rear = LRUNode(-1, -1)
        self.front.next = self.rear
        self.rear.prev = self.front

    # If key in nodes, move to front of our linked list and return val. Else, return -1
    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.removeFromList(node)
            self.insertIntoFront(node)
            return node.val
        
        else:
            return -1
        
    # If key in nodes, update and move to front of our linked list
    #   Otherwise, check if adding key would cause a cache eviction
    #       If so, evict it. Then add new key to front
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:             # similar to get()        
            node = self.nodes[key]
            self.removeFromList(node)
            self.insertIntoFront(node)
            node.val = value

        else: 
            if len(self.dic) >= self.cap:
                self.removeFromRear()

            node = LRUNode(key, value)
            self.nodes[key] = node
            self.insertIntoFront(node)

    # Helper functions for readability and to avoid code repetition
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoFront(self, node):
        frontNext = self.front.next 
        self.front.next = node 
        node.prev = self.front 
        node.next = frontNext 
        frontNext.prev = node
    
    def removeFromRear(self):
        if len(self.nodes) == 0: return
        rearNode = self.rear.prev
        del self.nodes[rearNode.key]
        self.removeFromList(rearNode)


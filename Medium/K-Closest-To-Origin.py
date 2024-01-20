import heapq

class Solution:

    # Calculate distances, store in a minheap, pull k-smallest
    #   Don't need to use full Euclidean distance forumula, squaring x and y and summing them is sufficient
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # Add distances from origin to heap
        for x,y in points:
            distance = (x * x + y * y)
            heap.append((distance, x, y))

        heapq.heapify(heap)
        smallest = heapq.nsmallest(k, heap)

        return [(i[1], i[2]) for i in smallest]
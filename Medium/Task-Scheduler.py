class Solution:

    # Another Greedy Solution. Greedyily schedule the task with most runs left
    #   Use a heap to do this efficiently
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        # Counter to get a hashmap of tasks to runs
        counter = Counter(tasks)
        time = 0

        # Add runs to heap. Negative to imitate a max heap
        for val in counter.values():
            heapq.heappush(pq, -val)

        # While there are runs left
        while pq:
            # A cycle is one more than the idle time
            cycle = n + 1
            nextRound = []

            # Get the top prio item, decrement it. If it still needs to be run, add it to nextRound
            while pq and cycle:
                item = -heapq.heappop(pq)
                item -= 1
                if item:
                    nextRound.append(item)
            
                cycle -= 1
                time += 1

            # Add everything in nextRound back into the heap
            for item in nextRound:
                heapq.heappush(pq, -item)
            
            if not pq: break
            time += cycle
        
        return time


                    
                        
                        
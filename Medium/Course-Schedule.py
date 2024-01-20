class Solution:

    # This is esentially cycle detection. Create a graph, traverse it with DFS. 
    #   If we find a cycle, we cannot finish all courses. Otherwise, we can
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        visited = set()
        explored = set()

        # Our helper dfs function
        def dfs(course):
            # Check if we've seen this course already
            if course in visited:
                # If we've seen this course AND have not finished exploring it, we have a cycle, terminate
                if course not in explored:
                    return False
                # Otherwise, we've seen the course and finished exploring it, so no cycle, we can return True
                return True

            # This executes if course has not been seen yet           
            visited.add(course)
            # Core DFS, call on neighbors
            for neighbor in courses[course]:
                if not dfs(neighbor): return False
            
            # Add to explored after all neighbors have been evaluated
            explored.add(course)
            return True
        
        # Create graph representation. If [0, 1] is a pair, to take 1 we must take 0. So add 0->1 as an edge
        for prereq in prerequisites:
            courses[prereq[1]].append(prereq[0])
        
        # Call DFS on any number not yet explored. We can't just call it on zero as the graph is not necessarily connected
        for i in range(numCourses):
            if i not in explored:
                if not dfs(i):
                    return False
        
        return True
            

        
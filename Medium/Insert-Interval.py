class Solution:

    # Input array is already sorted, so we can iterate through it and add each interval
    #   before the new interval to output, then the new interval while merging any overlaps,
    #   and finally all intervals after the new interval
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
			# interval occurs wholly before newInterval, so we can add the current interval
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # interval occurs wholly after newInterval, so we add newInterval and update it
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            # Overlap, so we choose the min for start and max for end of newInterval 
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result
        
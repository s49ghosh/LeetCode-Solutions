class Solution:

    # Sort by start time, append one at a time to the answer. If there is an overlap, merge
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for interval in intervals:
            # Either ans is empty, or the last interval is ans ends before the 
            #   current one starts, so we are free to add
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)

            # Otherwise, current interval starts before last interval ends.
            #   Since they're sorted by start, we just need to set the last interval's end
            #   to the max of both end times to complete the merge
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans
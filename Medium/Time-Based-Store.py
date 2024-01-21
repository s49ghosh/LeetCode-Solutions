class TimeMap:

    # For each key, store values sorted by timestamp. To find a value, do a binary search on timestamp
    def __init__(self):
        self.store = defaultdict(list)

    # Timestamps strictly increase, so just append
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    # If key is in store, get values. Then do a binary search for timestamp
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        values = self.store[key]
        index = bisect.bisect_right(values, timestamp, key=lambda x: x[0])
		
        if not index: return ''
        return values[index - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
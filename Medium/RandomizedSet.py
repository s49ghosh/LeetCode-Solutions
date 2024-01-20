class RandomizedSet:

    # A Set would be great for insert and remove, but we can't get a random element in O(1)
    #   Instead use a combination of a hashmap and an array. We can get a random element from an array in O(1)
    #   But removal from an array is not O(1).. or is it? It is if we remove from the back of the array.
    #   The array will store the values, the hashmap will map values to their indices.
    def __init__(self):
      self.arrayStore = []
      self.dictStore = {}
        
    def insert(self, val: int) -> bool:
      # Item is already in the RandomizedSet
      if val in self.dictStore: return False
      
      self.arrayStore.append(val)
      self.dictStore[val] = len(self.arrayStore)
      
      return True
        

    def remove(self, val: int) -> bool:
      # RandomizedSet is empty
      if not self.arrayStore: return False
      # Item is not in the RandomizedSet
      if val not in self.dictStore: return False
      
      idx = self.dictStore[val]
      numAtEnd = self.arrayStore[-1]
      
      # Put what used to be at the end at the removed val's index
      self.arrayStore[idx] = numAtEnd
      self.dictStore[numAtEnd] = idx

      # Remove val
      self.arrayStore.pop()
      self.dictStore.pop(val)
      
      return True
        

    def getRandom(self) -> int:
      return random.choice(self.arrayStore)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
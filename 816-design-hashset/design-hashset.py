class MyHashSet:

    def __init__(self):
        self.hashset = []
        

    def add(self, key: int) -> None:

        if self.contains(key):
            return
        else:
            self.hashset.append(key)

        

    def remove(self, key: int) -> None:

        for index,k in enumerate(self.hashset):
            if k == key:
                self.hashset.pop(index)
                return
        

    def contains(self, key: int) -> bool:

        for k in self.hashset:
            if k == key:
                return True
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
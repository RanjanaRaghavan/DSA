class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = list(range(1, 1001))
        heapq.heapify(self.min_heap)
        

    def popSmallest(self) -> int:
            return heapq.heappop(self.min_heap)
        

    def addBack(self, num: int) -> None:
        if num not in self.min_heap:
            heapq.heappush(self.min_heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
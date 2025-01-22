class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderd_dic = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.orderd_dic:
            return -1
        
        self.orderd_dic.move_to_end(key)
        return self.orderd_dic[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.orderd_dic:
            self.orderd_dic.move_to_end(key)
        
        self.orderd_dic[key] = value

        #Logic to evict
        if len(self.orderd_dic) > self.capacity:
            self.orderd_dic.popitem(False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
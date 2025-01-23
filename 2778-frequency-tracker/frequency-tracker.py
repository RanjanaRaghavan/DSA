class FrequencyTracker:

    def __init__(self):
        self.num_array = [0] * (10 ** 5 + 1)
        self.freq_array = [0] * (10 ** 5 + 1)
        
    def add(self, number: int) -> None:
        old_freq = self.num_array[number]
        self.num_array[number] +=1
        #change freq arr also
        freq = self.num_array[number]
        self.freq_array[freq] +=1
        self.freq_array[old_freq] -=1

    def deleteOne(self, number: int) -> None:
        if self.num_array[number] > 0:
            old_freq = self.num_array[number]
            self.num_array[number] -=1
            self.freq_array[old_freq] -=1
            self.freq_array[self.num_array[number]] +=1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_array[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        count = 0
        for i in range(1,max(arr)+1):
            #print(i,count)
            if i not in arr:
                count +=1
            
            if count == k:
                return i
        
        #find missing nums after the loop
        return arr[-1] + (k - count)

        


        
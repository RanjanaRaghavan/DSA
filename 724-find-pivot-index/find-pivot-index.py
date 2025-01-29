class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = []
        suffix_sum = []

        #Prefix Sum
        p_sum = 0
        for num in nums:
            p_sum += num
            prefix_sum.append(p_sum)

        #Suffix Sum
        s_sum = 0
        for num in nums[::-1]:
            s_sum += num
            suffix_sum.append(s_sum)

        suffix_sum = suffix_sum[::-1]

        print(prefix_sum, suffix_sum)

        for i in range(len(prefix_sum)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        
        return -1
        
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for start in range(1,10):
            self.generate_number(start,n,result)
        return result


    def generate_number (self, cur_num, limit, result):

        if cur_num > limit:
            return
        else:
            result.append(cur_num)
        
        #next number
        for nxt_dig in range(10):
            nxt_num = cur_num * 10 + nxt_dig
        
            if nxt_num > limit:
                break
            else:
                self.generate_number(nxt_num,limit,result)


        
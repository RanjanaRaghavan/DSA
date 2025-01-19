class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        map1 = {
            1:set("qwertyuiop"),
            2:set("asdfghjkl"),
            3:set("zxcvbnm")
        }

        output = []
        wordSet =0
        for word in words:
            low_word = word.lower()
            if low_word[0] in map1[1]:
                wordSet = 1
            if low_word[0] in map1[2]:
                wordSet =2
            if low_word[0] in map1[3]:
                wordSet = 3
            count =0
            for char in low_word:
                if wordSet == 0 or char not in map1[wordSet]:
                    break
                else:
                    count +=1
            if count == len(word):
                output.append(word)
                
        return output
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowelSet = set("aeiou")

        s_list = list(s)
        
        start = 0
        end = len(s)-1

        while start < end:

            while s_list[start].lower() not in vowelSet and start<end:
                start +=1
            
            while s_list[end].lower() not in vowelSet and start < end:
                end -=1

            
            s_list[start],s_list[end] = s_list[end],s_list[start]
            
            start +=1
            end -=1

        return ''.join(s_list)

        
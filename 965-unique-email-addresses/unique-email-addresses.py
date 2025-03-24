class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        '''
            1. split domain and localname delimeter -> @
            2. Reframe domain and local name according to rules
            3. Add them to a set to filter duplicates 
        '''

        set1 = set()

        for email in emails:

            local , domain = email.split("@")
            #print(local,domain)

            local = local.split("+")[0]
            local = local.replace(".","")
            print(local+"@"+domain)
            set1.add(local+"@"+domain)
        
        return len(set1)



        
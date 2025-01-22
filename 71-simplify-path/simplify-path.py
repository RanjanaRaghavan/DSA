class Solution:
    def simplifyPath(self, path: str) -> str:

        #A stack for path
        canonical_path = []

        path_list = path.split('/')
        
        for p in path_list:
            if p == '.':
                continue
            elif p == '':
                continue 
            elif p == '..':
                if len(canonical_path):
                    canonical_path.pop()
            else:
                canonical_path.append(p)
            

        return '/' + '/'.join(canonical_path)
        
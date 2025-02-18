class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image or image[sr][sc] == color:
            return image
        
        Q = collections.deque([[sr,sc]])
        ogcolor = image[sr][sc]
        
        while Q:

            cur_size = len(Q)

            for _ in range(cur_size):

                #Get the position, and change its color
                node = Q.popleft()
                r = node[0]
                c = node[1]
                image[r][c] = color

                #Add its neighbours who share same og color

                #up
                if r-1 >= 0 and image[r-1][c] == ogcolor:
                    Q.append([r-1,c])
                #down
                if r+1 < len(image) and image[r+1][c] == ogcolor:
                    Q.append([r+1,c])

                #right
                if c+1 < len(image[0]) and image[r][c+1] == ogcolor:
                    Q.append([r,c+1])

                #left
                if c-1 >= 0 and image[r][c-1] == ogcolor:
                    Q.append([r,c-1])
        
        return image

                



        
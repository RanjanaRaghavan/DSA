class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = set()
        stack = [0]

        while(stack):

            room = stack.pop()

            if room not in seen:
                stack.extend(rooms[room])
                seen.add(room)
        
        return len(rooms) == len(seen)

        
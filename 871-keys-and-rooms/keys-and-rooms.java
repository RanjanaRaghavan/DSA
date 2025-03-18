class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {

        Set <Integer> seen = new HashSet<>();
        Deque<Integer> stack = new ArrayDeque<>();

        seen.add(0);
        stack.push(0);

        while(!stack.isEmpty()){

            int room = stack.pop();
            for(int key : rooms.get(room)){

                if(!seen.contains(key)){
                    seen.add(key);
                    stack.push(key);
                }
            }
        }
        
        return rooms.size() == seen.size();
    }
}
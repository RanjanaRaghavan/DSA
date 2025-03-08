class Solution {
    public boolean isValid(String s) {

        HashMap<Character, Character> map1 = new HashMap<>();
        map1.put('(', ')');
        map1.put('[', ']');
        map1.put('{', '}');

        Stack<Character> stack1 = new Stack<>();

        for (char c : s.toCharArray()) {

            if (map1.containsKey(c)) {
                stack1.push(c);
            } else {
                if (stack1.size() > 0) {

                    char top = stack1.pop();
                    if (map1.get(top) != c) {
                        return false;
                    }

                }
                else{
                    return false;
                }

            }
        }

        return stack1.isEmpty();

    }
}
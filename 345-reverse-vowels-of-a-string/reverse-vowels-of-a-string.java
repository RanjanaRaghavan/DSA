class Solution {
    public String reverseVowels(String s) {
        
        int start = 0;
        int end = s.length() -1;

        char[] str = s.toCharArray(); 
        HashSet<Character> set = new HashSet<>();
        set.add('a');
        set.add('e');
        set.add('i');
        set.add('o');
        set.add('A');
        set.add('E');
        set.add('I');
        set.add('O');
        set.add('U');
        set.add('u');

        while(start < end){

            while(!set.contains(str[start]) && start < end){
                start++;
            }
            while(!set.contains(str[end]) && start < end){
                end--;
            }

            char temp = str[start];
            str[start] = str[end];
            str[end] = temp;

            start++;
            end--;

        }

        return new String(str);
    }
}
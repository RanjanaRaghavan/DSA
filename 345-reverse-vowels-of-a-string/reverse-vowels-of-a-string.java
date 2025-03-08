class Solution {
    public String reverseVowels(String s) {

        char[] str = s.toCharArray(); 
        HashSet<Character> set1 = new HashSet<>();

        set1.add('a');
        set1.add('e');
        set1.add('i');
        set1.add('o');
        set1.add('u');
        set1.add('A');
        set1.add('E');
        set1.add('I');
        set1.add('O');
        set1.add('U');

        int start = 0;
        int end = s.length()-1;

        while(start<end){

            while(!set1.contains(str[start]) && start<end){
                start++;
            }
            while(!set1.contains(str[end]) && start<end){
                end--;
            }

            char temp = str[start];
            str[start]= str[end];
            str[end] = temp;

            start++;
            end--;
        }
        
        return new String(str);
    }
}
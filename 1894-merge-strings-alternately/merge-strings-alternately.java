class Solution {
    public String mergeAlternately(String word1, String word2) {

        StringBuilder str = new StringBuilder();
        int l = Math.min(word1.length(), word2.length());

        for(int i =0;i<l;i++){
            str.append(word1.charAt(i));
            str.append(word2.charAt(i));
        }

        if(l< word1.length()){
            str.append(word1.substring(l));
        }
        else{
            str.append(word2.substring(l));
        }

        return str.toString();
        
    }
}
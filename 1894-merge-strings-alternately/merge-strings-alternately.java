class Solution {
    public String mergeAlternately(String word1, String word2) {

        int l1 = word1.length();
        int l2 = word2.length();
        int l = Math.min(l1,l2);

        StringBuilder merged = new StringBuilder();

        for(int i=0;i<l;i++){
            merged.append(word1.charAt(i));
            merged.append(word2.charAt(i));
        }

        if(l1 > l2){
            merged.append(word1.substring(l));
        }
        else{
            merged.append(word2.substring(l));
        }

        return merged.toString();
    }
}
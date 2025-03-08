class Solution {
    public int largestAltitude(int[] gain) {

        int sum = 0;
        int max = 0;
        
        for(int g : gain){
            sum = sum + g;
            max = Math.max(max,sum);
        }

        return max;
        
    }
}
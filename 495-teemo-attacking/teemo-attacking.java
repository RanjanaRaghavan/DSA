class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {

        int poison = 0;

        for(int i=0;i<timeSeries.length-1;i++){

            int gap = timeSeries[i+1] - timeSeries[i];
            if(gap < duration){
                poison += gap;
            }
            else{
                poison += duration;
            }
        }

        //Last attack
        poison += duration;

        return poison;
        
    }
}
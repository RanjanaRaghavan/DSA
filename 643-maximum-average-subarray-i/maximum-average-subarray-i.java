class Solution {
    public double findMaxAverage(int[] nums, int k) {

        int maxSum = Integer.MIN_VALUE;
        for(int i =0;i<=nums.length-k;i++){

            int tempSum = sum(i,nums,k);
            maxSum = Math.max(maxSum,tempSum);

        }
        System.out.println(maxSum);
        return (double) maxSum/k;
        
    }

    public int sum(int start,int[] nums,int k){

        int sum = 0;
        for(int i=start;i<start+k;i++){
            sum = sum + nums[i];
        }
        return sum;
    }
}
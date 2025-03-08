class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap <Integer,Integer> map1 = new HashMap<>();

        for(int i =0;i<nums.length;i++){

            int comp = target - nums[i];

            if(map1.containsKey(comp)){
                return new int[] {i,map1.get(comp)};
            }

            map1.put(nums[i],i);
        }
        return new int[] {};
    }
}
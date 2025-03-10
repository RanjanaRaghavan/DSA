class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {

        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();

        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        ArrayList<Integer> arr2 = new ArrayList<Integer>();

        for(int i=0;i<nums1.length;i++){
            set1.add(nums1[i]);
        }  
        for(int i=0;i<nums2.length;i++){
            set2.add(nums2[i]);
        }

        for(int num : set1){

            if(!set2.contains(num)){
                arr1.add(num);
            }
        }

        for(int num : set2){

            if(!set1.contains(num)){
                arr2.add(num);
            }
        }
        
        return Arrays.asList(arr1,arr2);
    }
}
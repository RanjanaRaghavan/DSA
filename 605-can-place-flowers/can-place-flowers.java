class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        //Base cases
        if(n == 0){
            return true;
        }

        if(n > flowerbed.length){
            return false;
        }

        for(int i =0;i<flowerbed.length;i++){

            if(flowerbed[i] == 0  && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.length -1 || flowerbed[i+1] == 0)){
                flowerbed[i] =1;
                n = n-1;
                i++;
            }

            if(n == 0){
                return true;
            }

        }


        return n == 0;
        
    }
}
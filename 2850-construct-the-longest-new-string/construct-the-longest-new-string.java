class Solution {
    public int longestString(int x, int y, int z) {

        if(x == y){
            return (x*2 + z) *2;
        }
        else{
            return (Math.min(x,y)*2 + z) *2 + 2; //+2 bcuz AB at the end or beginning
        }
        
    }
}
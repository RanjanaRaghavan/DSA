class Solution {
    public boolean isSubsequence(String s, String t) {

        //Base Case
        int l1 = s.length();
        int l2 = t.length();
        
        if(l1 ==0 || (l1 ==0 && l2==0)){
            return true;
        }

        if(l2 ==0){
            return false;
        }

        char[] tt = t.toCharArray();
        char[] ss = s.toCharArray();
        int p1 = 0;
        int count = 0;

        for(int p2 =0;p2<l2;p2++){

            if(tt[p2] == ss[p1]){
                count++;
                p1++;
            }

            if(p1 == l1){
                return true;
            }
        }

        return false;
        
    }
}
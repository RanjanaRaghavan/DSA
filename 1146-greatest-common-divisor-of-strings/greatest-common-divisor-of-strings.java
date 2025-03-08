import java.math.BigInteger;
class Solution {
    public String gcdOfStrings(String str1, String str2) {

        
        //Base Case
        if(!(str1 + str2).equals(str2 + str1)){
            System.out.println(str1 + str2);
            return "";
        }
        
        int gcd = BigInteger.valueOf(str1.length()).gcd(BigInteger.valueOf(str2.length())).intValue();

        return str1.substring(0,gcd);
    }
}
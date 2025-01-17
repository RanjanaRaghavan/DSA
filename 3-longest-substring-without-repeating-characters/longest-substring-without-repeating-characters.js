/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    let set1 = new Set();
    let maxCount =0;

    let left =0
    let right =0
    while((left <=right && right <= s.length-1)){
        let count =0
        while(!set1.has(s[right])){
            //console.log(s[right])
            set1.add(s[right]);
            if(right <s.length-1)
                right++;
            else
                break;
            //console.log("inside",right)
        }
        
        maxCount = Math.max(maxCount,set1.size);

        set1.delete(s[left]);
        //console.log(set1,right,left)

        if(right >= s.length-1)
            break;
        else
            left++;
        
    }
    
    return maxCount;
};
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function(s, k) {
    
    if(s.length < k)
        return false;
    if (s.length === k) 
        return true;
    
    let map1 = new Map();

    for(let i=0;i<s.length;i++)
        map1.set(s[i], (map1.get(s[i]) || 0) +1);

    let countWithOdd =0;
    for(let value of map1.values()){
        if(value %2 !== 0)
            countWithOdd++;
    }

    if(countWithOdd > k)
        return false;
    
    else
        return true;
};
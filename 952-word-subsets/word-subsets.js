/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {

    let result = [];
    let map1 = new Map();

    //Map for all the letters of all words in word2;
    for(let i=0;i<words2.length;i++){
        let tempMap = new Map();
        for(let j=0;j<words2[i].length;j++)
            tempMap.set(words2[i][j], (tempMap.get(words2[i][j])|| 0)+1); 
        
        for (let [char, count] of tempMap) {
            map1.set(char, Math.max(map1.get(char) || 0, count));
        }
    }
    
    //Loop through words1 and check every word map
    for(let i=0;i<words1.length;i++){
        let map2 = new Map();

        //Add the letters in every word to the map.
        for(let j=0;j<words1[i].length;j++)
            map2.set(words1[i][j], (map2.get(words1[i][j])|| 0)+1); 

        //Check if the count of letters match and not more than in word1
        let flag = true;
        for (let [char, count] of map1) {
            if ((map2.get(char) || 0) < count) {
                flag = false;
                break;
            }
        }
            if(flag == true)
                result.push(words1[i]);
        }
    return result;
};
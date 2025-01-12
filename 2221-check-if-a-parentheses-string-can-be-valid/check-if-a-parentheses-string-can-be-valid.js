/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function(s, locked) {
    // Odd length strings cannot form valid parentheses
    if (s.length % 2 !== 0) return false;
    
    // Forward pass
    let open = 0; // Tracks available '(' or unlocked indices
    for (let i = 0; i < s.length; i++) {
        if (locked[i] === '0' || s[i] === '(') {
            open++; // Treat as an opening parenthesis
        } else {
            open--; // Closing parenthesis needs a match
        }
        if (open < 0) return false; // Too many closing parentheses
    }
    
    // Backward pass
    let close = 0; // Tracks available ')' or unlocked indices
    for (let i = s.length - 1; i >= 0; i--) {
        if (locked[i] === '0' || s[i] === ')') {
            close++; // Treat as a closing parenthesis
        } else {
            close--; // Opening parenthesis needs a match
        }
        if (close < 0) return false; // Too many opening parentheses
    }

    return true; // Passed both forward and backward checks
};

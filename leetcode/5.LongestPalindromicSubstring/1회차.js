

/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
   function isPalindrome(s) {
     const target = s.split('').reverse().join('')
     if (s === target) {
       return true
     }
     return false
   }

   const results = {}
   for(let i=0; i<s.length; i++) {
     for(let j=j; j<s.length+1; j++) {
       const subString = s.slice(i, j)
       if(isPalindrome(subString)) {
         results[subString] = subString.length
       }
     }
   }

  //  return Object.entries(results).max()
};

// longestPalindrome('abhcchchh')
longestPalindrome('abba')
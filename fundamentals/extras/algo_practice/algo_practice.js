// Algo 1


/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(a, b) {
    return a.toLowerCase() == b.toLowerCase();
}


// Algo 2

/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
// function reverseString(str) {
  //   return str.split("").reverse().join("")
  // }
  
const str1 = "creature";
function reverseString(str) {
  midPoint = Math.floor(str.length/2)
  newStr = str[midPoint]
  for(var i = 1; newStr.length < str.length; i++){
    if (str[midPoint+i]){
      newStr = str[midPoint+i] + newStr
    }
    newStr = newStr + str[midPoint-i]
    console.log("new string", newStr)
  }
  return newStr
}
console.log(reverseString(str1))
/* 'hello' -> 'olleh' */
function reverse(str) {
    /* First method */
    // return str.split('').reverse().join('')

    /* Second method */
    // let result = ''
    // for (let i = str.length-1; i >= 0; i--) {
    //     result = result + str[i]
    // }
    // return result

    /* Another version of for loop */
    // result = ''
    // for (let char of str) {
    //     result = char + result
    // }
    // return result

    /* Higher order array methods */
    // let result = ''
    // str.split('').forEach(char => result = char + result)
    // return result

    return str.split('').reduce((result, char) => char+result, '')
}


/* str = 'racecar' */
function isPalindrome(str) {
    const result = str.split('').reverse().join('')
    return result === str
}

/* 521 -> 125 */
function reverseInt(int) {
    const result = parseInt(int.toString().split('').reverse().join('')) * Math.sign(int)
    return result
}

/* 'i love javascript' -> 'I Love Javascript' */
function capitalizeLetters(str) {
    /* First method */
    // strArr = str.toLowerCase().split(' ')
    // for (let i = 0; i < strArr.length; i++) {
    //     strArr[i] = strArr[i].substring(0,1).toUpperCase() + strArr[i].substring(1)
    // }
    // return strArr.join(' ')

    /* Higher order function */
    return str
    .toLowerCase()
    .split(' ')
    .map((word) => word[0].substring(0,1).toUpperCase() + word.substr(1))
    .join(' ')
}

/* maxCharacter('javascript') => 'a' */
function maxCharacter(str) {
    const charMap = {}
    let maxNum = 0
    let maxChar = ''

    str.split('').forEach((char) => {
        if (charMap[char]) {
            charMap[char]++
        } else {
            charMap[char] = 1
        }
    })
    
    for (let char in charMap) {
        if (charMap[char] > maxNum) {
            maxNum = charMap[char]
            maxChar = char
        }
    }
    return maxChar
}

/* longestWord('hello, my name is sam') => 'hello'
    longestWord('hello, my name is samip') => ['hello', 'samip']
 */
function longestWord(sen) {
    const wordArr = sen.toLowerCase().match(/[a-z0-9]+/g)

    // Sort by length
    const sorted = wordArr.sort((a, b) => {
        return b.length - a.length
    })

    // If multiple words then put into arraay
    const longestWordArr = sorted.filter((word) => {
        return word.length === sorted[0].length
    })

    return longestWordArr.length === 1 ? longestWordArr[0] : longestWordArr
}

/* chunkArray([1,2,3,4,5], 2) => [[1,2], [3,4], [5]]*/
function chunkArray(arr, len) {
    /* Solution 1 */
    let chunkedArr = []
    let i = 0

    while(i < arr.length) {
        chunkedArr.push(arr.slice(i, i+len))
        i = i + len
    }
    return chunkedArr
}

function flattenArray(arrays) {
    /* Using reduce */
    // return arrays.reduce((a, b) => a.concat(b))

    // Method 2 - Apply method
    // return [].concat.apply([], arrays)

    // Method 3 - Spread operator
    return [].concat(...arrays)
}

/* 'elbow' => 'below'
 */
function isAnagram(str1, str2) {
    return formatStr(str1) === formatStr(str2)
}

/** Helper function */
function formatStr(str) {
    return str
    .replace(/[^\w]/g, '')
    .toLowerCase()
    .split('')
    .sort()
    .join('')
}

/** Changes every letter of the string to the one that follows it and capitalize the vowels 
 * ex - 'hello there' === 'Ifmmp UIfsf'
*/
function letterChanges(str) {
    let newStr = str.toLowerCase().replace(/[a-z]/gi, (char) => {
        if (char === 'z' || char === 'Z') {
            return 'a'
        } else {
            return String.fromCharCode(char.charCodeAt() + 1)
        }
    })

    newStr = newStr.replace(/a|e|i|o|u/gi, (vowel) => {
        return vowel.toUpperCase()
    })
    return newStr
}

/** addAll(2,5,6,7) == 20  */
function addAll(...numbers) {
    //  forEach
    // let total = 0
    // numbers.forEach((num) => total += num)
    // return total

    // reduce
    return numbers.reduce((acc, cur) => {
        return acc + cur
    })
}

function sumAllPrimes(num) {
    let total = 0
    
    function checkForPrime(i) {
        for (j = 2; j < i; j++) {
            if (i % j === 0) {
                return false
            }
        }
        return true
    }

    for (let i = 2; i <= num; i++) {
        if (checkForPrime(i)) {
            total = total + i
        }
    }
    return total
}

console.log(sumAllPrimes(10))
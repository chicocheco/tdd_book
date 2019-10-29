# 21, 22, 23, 24, 25 / strings in JS

## Lowercase, uppercase methods
- the JS version of str.lower() from Python we have **myString.toLowerCase();**
- the JS version of str.upper() from Python we have **myString.toUpperCase();**

In Python we could use string.capitalize() to do this:
```js
var firstChar = cityToCheck.slice(0, 1);
var otherChars = cityToCheck.slice(1);
firstChar = firstChar.toUpperCase();
otherChars = otherChars.toLowerCase();
var cappedCity = firstChar + otherChars;
```

## Slicing strings like arrays
- notice that we can use .slice() both on arrays as well as on string
- passing only 1 argument to .slice() means we want to slice the string to the end no matter how long it is
- in Python, string[3:] = make a slice from the 4th character to the end (0-based)
- in JS, string.slice(3); = make a slice from 4th character to the end (0-based)
- 'string'[0:1] or 'string'[0] equals "string".slice(0, 1);
- number of characters we are slicing is always the 1st index subtracted from the 2nd 
- 10th character of a string has an index 9 cos length is 1-based, indices 0-based
- number of characters = amount of characters

How to loop over a string to check for double spaces
```js
var str = prompt("Enter some text");
var numChars = str.length;
for (var i = 0; i < numChars; i++) {
  if (str.slice(i, i + 2) === "  ") {
    alert("No double spaces!");
    break;
  }
}
```

## Finding segments 

- in Python we use .find() or .index() to find the lowest index, only the **first occurrence** 
- **.index()** raises ValueError if nothing found, .find() returns "-1" in that case
- in JS we use .indexOf("substring"); and it behaves almost identical to .index() from Python

- but there is also a method to search for an index of a substring from the end (right side) of the string .lastIndexOf();
- in Python we have .rfind() and .rindex() to do this
- can be found !== -1

To test whether a string can be found within another string we use **string.indexOf("substring") !== -1**
```js
var firstChar = text.indexOf("World War II");
if (firstChar !== -1) {
  text = text.slice(0, firstChar) + "the Second World War" + text.slice(firstChar + 12);
  // where 12, because "World War II".length; would return 12
}
```

1. in this snippet we take first slice until the substring to be replaced where the second index is the first index of the substring
2. now we concatenate it with a new string so we skip the original substring
3. now we concatenate it with the rest of the original string and we use .slice() with one index only (to reach the end), adding 12 because that is how the new substring is long

## Index of a single character

- in Python with brackets as in 'string'[0] or 'string'[-1] for the first or last characters
- in JS by .charAt(0) or .chartAt('string'.length - 1)

example of charAt, alternative is .push() to keep adding to the end of an array
```js
var str = 'prdel na hrnec';
var myArray = [];
for (var i = 0; i < str.length; i++) {
  myArray[i] = str.charAt(i);
  // myArray.push(str.charAt(i));
}
```

## replace method in JS and /substring/g syntax for global replace

- in JS we can use the same method to directly replace a string by another by .replace()
- this method works only with the first occurrence when the segment enclosed by ""
- this method works only with all occurrences when the segment enclosed by //g
- in Python the latter is the default behavior (all occurrences at once)
- same as in Python, when replacing we get a new copy rather than a modified original variable

example:
```js
// first occurrence:
text = text.replace("World War II", "the Second World War");
// all at once:
var newText = text.replace(/World War II/g, "the Second World War");
```
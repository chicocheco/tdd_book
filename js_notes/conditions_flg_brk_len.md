# 18 / flag, break and length of an array in for loops

## we can use a "flag" to note that the state changed (switch)
- "flag" is a regular variable with 2 states: **true/"yes" or false/"no"**
- in JS it is all lowercase, in Python True and False

```js
// most common case is this
var matchFound = false;
```

## we can safe the computer from looping all the way to the end by "break"
- the keyword is identical to the one in Python and its function too: break;
- it termites the loop immediately

## we can only loop as many times as the array is long
- in JS we get the length of an array by its **.length** attribute
- in Python we wrap a list into len()

```js
var numElements = cleanestCities.length;
var matchFound = false;
for (var i = 0; i < numElements; i++) {
    if (cityToCheck === cleanestCities[i]) {
        matchFound = true;
        alert("It's one of the cleanest cities");
        break;
    }
}
if (matchFound === false) {
    alert("It's not on the list");
}
```
- the **.length** number is 1-based so we always use **<** because the i number is 0-based
- every semicolon ";" marks the end of one statement (or {} encloses it)
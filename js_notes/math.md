# 25, 26, 27, 28, 29, 30 Rounding numbers, random numbers, converting between strings and numbers, length of decimals

- to round a number to the nearest integer we use Math.round();
- Math.round() rounds up 1.5 to 2, -2.5 to -2 etc.
- Math.round() equals to a built-in round() and it works the same but Python does not round up 2.5 to 3

- to round *UP* to the nearest integer we use Math.ceil()
- to round *DOWN* to the nearest integer we use Math.floor()

- in Python we have the exact same equivalent but we must **import math** first
- in Python we have math.ceil() and math.floor()

## Generate random numbers

- in Python we would simply **import random** and random.randint(1, 6)
- in JS we use Math.random() to get a 16-decimal, we must multiply be 6, add 1 and round DOWN
- adding 1 ensures that there is the same chance to get 0 and 6 as the numbers in the middle
- otherwise we would never get 0 by rounding UP and 6 by rounding DOWN

```js
// this is what in Python we do with random.randint(0, 6):

var bigDecimal = Math.random();
var improvedNum = (bigDecimal * 6) + 1;  // random number from 0 to 6
var numberOfStars = Math.floor(improvedNum);
```

## Converting strings to integers and decimals and back to strings

- unlike Python, JS is capable to resolve strings as digits so even the following works
- Python is not forgiving and if we mix strings with digits, it does not work
```js
// returns 50, because - means, logically, only SUBTRACT
var profit = "200" - "150";

// also returns 50
var resultNum = "200" - 150;

// returns 200150, because + can be both ADD or CONCATENATE and the latter has a priority
var resultString = "200" - 150;
```
- the fact that CONCATENATING has this preference is not always desirable
- to make sure that a variable converts to an integer we use **parseInt()**
- unfortunately parseInt() **does not round** the integer so parseInt("1.9999"); returns 1 and not 2
- to preserve decimals we can use **parseFloat()** instead
- to avoid having to decide whether we need one or another, we use **Number();** which converts a string to integer or float

- in Python parseInt() = int() but it does not cut off decimals if there are, it does not work on them at all
- in Python, parseFloat() = float()
```js
// results in a string
var currentAge = prompt("Enter your age.");
var qualifyingAgeConcatenated = currentAge + 1;

// results in a digit as expected
var currentAge = prompt("Enter your age.");
var qualifyingAge = parseInt(currentAge) + 1;

// returns 1, not rounding it up or down, cuts off decimals
alert(parseFloat("1.9999"));
// returns 1.9999
alert(parseInt("1.9999"));

var floatingNumString = "24.9876";
var num = Number(floatingNumString);

var numberAsNumber = 1234;
var numberAsString = numberAsNumber.toString();
```
- to convert a number back to a string we use .toString(); method or str() in Python

## Controlling length of decimals
- shorten a number to 2 decimals with **.toFixed(2);**
- shorten a number to no decimals with **.toFixed();**
- .toFixed() returns a string

- if decimal ends in 5, it USUALLY rounds up but it DEPENDS on the browser
The workaround to make sure it always rounds UP:
```js
var str = num.toString();
// if the last char equals 5
if (str.charAt(str.length - 1) === "5") {
  // slice off the number except for the last char and append "6"
  str = str.slice(0, str.length - 1) + "6";
}
num = Number(str);
prettyNum = num.toFixed(2);
```
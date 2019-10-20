# 12 / if...else and else if statements in JS

## all-or-nothing with single "if":

```js
var x = prompt("Where does the Pope live?");
if (x === "Vatican") {
  alert("Correct");
}
```

nothing happens otherwise
## we can add the same condition with !== or use "else"
```js
if (x === "Vatican") {
  alert("Correct");
}
else {
  alert("Wrong answer!");
}
```
## when all tests above failed (more than 1 test) you want to test another condition (the "else if" statement)
```js
var correctAnswer = "Vatican";
if (x === correctAnswer) {
  alert("Correct!");
}
else if (x === "Rome") {
  alert("Incorrect but close");
}
else {
  alert("Incorrect");
}
```


### from Python where "else if" == "elif":
- Multiple if's means your code would go and check all the if conditions, where as in case of elif, if one if condition satisfies it would not check other conditions..

- in other words multiple elif's test for the first that results True and then skip the rest of elif's that follow
- while multiple if's test every "if" no matter if it results True or False 

#### we always assign value to a variable, not variable to a value

### more notes:
- if = "pokud"
- elif (else if) = "pokud ne, tak pak..."
- else = "jinak"
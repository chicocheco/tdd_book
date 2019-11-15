# 13, 14 / sets of conditions in JS

## combine more conditions with &&, to test all True
```js
if (weight > 300 && time < 6) {
    alert("Come to our tryout!");
}
else {
    alert("Come to our cookout!");
}
```

In Python we combine with "and"

## how to test for any True with ||
```js
if (SAT > avg || GPA > 2.5 || sport === "footbal") {
    alert("Welcome to Bubba State!");
}
else {
    alert("Have you looked into appliance repair?");
}
```

In Python we combine with "or"

### operators && and || can be combined and () give priority to tests

that means we can prioritize two conditions to be evaluated first before the others

### if statements can be nested, they replace &&

- every opening curly brackets means a new level in JS, in other words "{}" for nesting
- when you add level it is like another &&
- outer if = enclosing if
- inner if = nested if

```js
if (c === d) {
    if (x === y) {
        g = h;
        }
    else if (a === b) {
        g = h;
        }
    else {
        e = f;
        }
    }
else {
    e = f;
}
```
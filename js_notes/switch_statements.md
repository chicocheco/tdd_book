# 39, 40 Switch statements

- wherever you could use an if statement and its variations, you can use a switch statement
- the more conditions you need to test, the more we'll like the switch statement
- unlike if/else if/else, all **case** statements are run no matter if they are true or false
- (if **if** statement is truthful and it followed by another **if**, it is run too)
- (**else if** or **else** is executed only if the previous statements were not true)
- every time we want find truthful statement, we must **break** out of the **switch** statement
- **default** statement works like **else** (optional)
```js
if (dayOfWk === "Sat" || dayOfWk === "Sun") {
  alert("Whoopee!");
}
else if (dayOfWk === "Fri") {
  alert("TGIF!");
}
else {
  alert("Shoot me now!");
}

// that can be replaced by a switch statement, testing the value dayOfWk
// notice that case keyword is not indented 
switch(dayOfWk) {
case "Sat" :
  alert("Whoopee");
  break;
case "Sun" :
  alert("Whoopee");
  break;
case "Fri" :
  alert("TGIF!");
  break;
default :
  alert("Shoot me now!");
}
```

## there is no switch + case statements in Python, this might be the replacement
```python
def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 is default if x not found
```
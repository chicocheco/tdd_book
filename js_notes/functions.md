# 35, 36, 37, 38 Functions

- () are parentheses
- [] are brackets
- {} are curly brackets

```js
function tellTime() {
    const now = new Date();
    const theHr = now.getHours();
    const theMin = now.getMinutes();
    alert("Current time: "+ theHr + ":" + theMin);
}
// call the function
tellTime();

// function with an argument - the string we would pass like "Hello"
function greetUser(greeting) {
    alert(greeting);
}
greetUser("Hello");
```
- argument = data we pass to a function e.g. **"Hello"** string
- parameter that is a variable of a function e.g. **greeting**, it is used in the body of the function only
- we don't have to declare a parameter with **var** or **let**, it is implicit
- multiple arguments and parameters are matched up by their order

## Function can pass data back to the calling code by **return**
- a function in JavaScript cannot return more than a single value
- a variable has local scope when you declare it in a function, otherwise it is global
- variables declared by **let** have their scope in **the block** for which they are defined
- variables declared by **var** do not have this limitation

```js
function calcTot(merchTot) {
    let orderTot;
    if (merchTot >= 100) {
        orderTot = merchTot;
    }
    else if (merchTot < 50.01) {
        orderTot = merchTot + 5;
    }
    else {
        orderTot = merchTot + 5 + (.03 * (merchTot - 50));
    }
    return orderTot;
}
const totalToCharge = calcTot(79.99);
```




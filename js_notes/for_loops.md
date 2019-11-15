# 18 / for loops in JS

```js
for (let i = 0; i <= 4; i++) {
  if (cityToCheck === cleanestCities[i]) {
    alert("It's one of the cleanest cities");
  }
}
```

- "i" stands for "iteration" but can be whatever, it says where to start
- the second argument can be also "< 5", it says how many loops

this runs 5 times, finishes when i === 4, (0, 1, 2, 3, 4):
```js
for (let i = 0; i <= 4; i++) {}
```
this runs 4 times, finishes when === 3, (0, 1, 2, 3):
```js
for (let i = 0; i < 4; i++) {}
```

- the third argument "i++" **adds 1 AFTER each iteration** to "i" (likewise "++i" would add 1 in place)
- we use "i" here as an iteration and at the same time for getting values of elements by index

## in Python we use range() for this to loop over 0, 1, 2, 3, 4

```python
for i in range(5):
    print(i)
```
- we can go to negative numbers too, always put the counter first like in **x > -3**
```js
for (let x = 0; x > -3; i--) {
    // do something
}
```
in Python something like this
```python
for i in range(0, -3, -1):
    # do something
```
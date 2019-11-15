# 41, 42 While loops

- unlike with a for loop, while loop's counter is defined **before** the first line of while block
- similarly the counter is updated **within** the code that executes whe the loop runs
- all the how-to-loop directions in *for loops* are packed into the space between ()

```js
let i = 0;
while (i <= 3) {
    alert(i);
    i++;
}
```
In Python it works the same:
- while keyword followed by loop-limiting code (no parentheses here)
- counter defined before 
- counter updated within the while loop
```python
n = 5
while n > 0:
    n -= 1
    print(n)
```

## do ... while loops
- code in **do** block is **always executed** at least once, no matter what
- the loop-limiting code moves to the bottom 
- first iteration is guaranteed
```js
let i = 0;
do {
    alert(i);
    i++;
} while (i < 0);
```
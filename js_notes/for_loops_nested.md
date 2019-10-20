# 20 / nested for loops in JS

- The inner loop runs a complete cycle of iterations on each iteration of the outer loop
- the outer loop is like the minute hand of a clock
- the inner loop is the second hand
- if the outer loop runs 3x and the inner 5x, we get in total 15 iterations
- i and j are called counters and it continues like the alphabet I, J, K, L, M, N...
- inner and outer loop **don't share** the same counter (start with "i" for outer loop, then "j" for inner and so on)

```js
var firstNames = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "];
var lastNames = ["Zzz", "Burp", "Dogbone", "Droop"];
var fullNames = [];
for (var i = 0; i < firstNames.length; i++) {
  for (var j = 0; j < lastNames.length; j++) {
    // add an element like "Zzz" to "BlueRay", then "Burp" and so on
    fullNames.push(firstNames[i] + lastNames[j]);
  }
}
```

result is:
BlueRay Zzz,BlueRay Burp,BlueRay Dogbone,BlueRay Droop,
Upchuck Zzz,Upchuck Burp,Upchuck Dogbone,Upchuck Droop,
Lojack Zzz,Lojack Burp,Lojack Dogbone,Lojack Droop,
Gizmo Zzz,Gizmo Burp,Gizmo Dogbone,Gizmo Droop,
Do-Rag Zzz,Do-Rag Burp,Do-Rag Dogbone,Do-Rag Droop

- concatenate = "zřetězit"
- add = "sečíst"

## there are two ways of doing this exercise

```js
var animals = ["goat", "cat", "crow"];
var products = ["milk", "cheese", "burger"];
var foodItems = [];
var k = 0;

for (var i = 0; i < animals.length; i++) {
  for (var j = 0; j < products.length; j++) {
    foodItems.push(animals[i] + products[j]);
    k++;
  }
}
alert(foodItems);
// goatmilk,goatcheese,goatburger,catmilk,catcheese,catburger,crowmilk,crowcheese,crowburger

// another way:
var animals = ["goat", "cat", "crow"];
var products = ["milk", "cheese", "burger"];
var foodItems = [];
var k = 0;

for (var i = 0; i < animals.length; i++) {
  for (var j = 0; j < products.length; j++) {
    foodItems[k] = animals[i] + products[j];
    k++;
  }
}

alert(foodItems);
// goatmilk,goatcheese,goatburger,catmilk,catcheese,catburger,crowmilk,crowcheese,crowburger
```
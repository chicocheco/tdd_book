# 15 / arrays in JS

## like list() in Python

- "values" inside are not called neither "values" nor "items"
- they are "elements"
- when looking up a non-existing element, we get "undefined" error, in Python "index out of range"
- while in JS you can add elements to an empty list defining their index, in Python you cannot
- in Python you cannot add say "this element will have this index" if not element with that index existed already but in JS you can

## adding and removing from the end of an array
- in Python you use .append()/.extend() to add/extend by elements at the end of an array (from highest index), in JS **.push()**
- in Python you use **.pop()** to remove the last element and return it, in JS as well (returns it at the same time too)
- in JS if you assign an empty array a value at index 3, indices 0, 1 and 2 are filled with "undefined" meaning the length of this array will become 4 elements 

## adding and removing from the beginning of an array
- we remove elements to the beginning by **.shift()** 
- we add elements from the beginning by method **.unshift()**
- in Python not advised to do with "list", there are different data types for this

## inserting elements into arrays
- in JS there is a method combining inserting and optionally removing elements at the same time **.splice()** where, similarly to Python, first argument = inserting point, second argument = how many elements to remove from this index and finally third argument = what to insert
```js
// this does not remove anything, adding 3 elements at index 2 (3rd position)
let pets;
pets.splice(2, 0, "pig", "duck", "emu");
```
- the first index = where the inserted elements will start (replace element of this index, push rest further)
- the last index = the index *after* the last one to be inserted (element at this position unchanged)

## slicing arrays
- to slice an array use **.slice()** which exists in Python but not as a method, Pythonic is to use [:] brackets
- in python we first assign slice() to a variable and later we can use this variable in the brackets
- we get also get a single element by its index like in Python so myArray[0] gets the element of index 0
- **IMPORTANT: list in Python shrinks and extends as well as the range of indeces used to retrieve elements, in JS it is static**
## 56 Target all elements by tag name

We can select all elements at once, for example every 
 - paragraph `<p></p>`
 - image `<img>`
 - unordered list `<ul>`
 - and so on
```js
// to get an array-like collection
const par = document.getElementsByTagName('p');
// then we can access each <p> by its index
const textInMiddle = par[1].innerHTML;
// or directly change the text of the paragraph
par[1].innerHTML = "This SUV is too big.";
// or set a different font to all of them
for (let i = 0; i < par.length; i++) {
    par[i].style.fontFamily = "Verdana, Geneva, sans-serif";
}
```
```html
<p>This bed is too small.</p>
<p>This bed is too big.</p>
<p>This bed is just right.</p>
```

We can reduce the selection of every paragraph in a particular `<div>` element
```js
const e = document.getElementById('rules');
const paras = e.getElementsByTagName('p');
```
Another example with a table
```js
const t = document.getElementById('table9');
const cells = t.getElementsByTagName('td');
for (let i = 0; i < cells.length; i++) {
    cells[i].style.backgroundColor = 'pink';
}
```
# 64, 65, 66, 67, 68, 69 DOM - Document Object Model

## Counting elements
```js
// target some div by id
const parentNode = document.getElementById('d2');
const nodeList = parentNode.childNodes;
const howManyKids = nodeList.length;

// to count how many images are within the div
let numberPics = 0;
for (let i = 0; i < howManyKids; i++) {
    if (nodeList[i].nodeName.toLowerCase() === 'img') {
        numberPics++;
    }
}
```

## Attributes (has, get, set)
```html
<!--example of an element node with 4 attributes-->
<img id="obrazek" src="dan.gif" alt="Dan" height="42" width="42">
```
```js
// find out whether the element has a particular attributes like class
const target = document.getElementById('obrazek');
const hasClass = target.hasAttribute('class'); // false

// read a value of a particular attribute
const target = document.getElementById('obrazek');
const readAltAttribute = target.getAttribute('alt'); // Dan

// set a new value and read it
const target = document.getElementById('obrazek');
const setAtt = target.setAttribute('alt', 'algo');
alert(target.getAttribute('alt'));
```

## Attributes as a collection
- we can access all attributes as a collection v Attr objects by .attributes
- access elements by index and their names, values, type like any other node
- we can count attributes by .length
```js
const myAttrColl = document.getElementById("obrazek").attributes;
const howManyAttrs = myAttrColl.length;
alert(myAttrColl[1].nodeValue);  
// moje[1] is object Attr with attributes nodeName, nodeValue, nodeType etc.
// nodeType returns 2 here
```

## Adding nodes to DOM
- we create a new element node like `document.createElement('p');`
- we create a new text node like `document.createTextNode('hello!')`
- we place text to a paragraph like `parNode.appendChild(newTextNode);`
- be aware that appending places the child always at the end
```js
const parentDiv = document.getElementById("div1");
const newParagraph = document.createElement("p");
const t = document.createTextNode("Hello world!");
newParagraph.appendChild(t);  // append text to paragraph
parentDiv.appendChild(newParagraph);  // now to div (element node)
```

## Inserting nodes to DOM
- if we want to place a node elsewhere than at the end we use `insertBefore()`
- we can remove a child by `removeChild()`
```js
const parentDiv = document.getElementById("div1");
const newParagraph = document.createElement("p");
const t = document.createTextNode("Hello world!");
newParagraph.appendChild(t);
paragraph1 = parentDiv.firstChild;
// insert a new elemente node consisting of a new text node
// BEFORE the first child, before paragraph1
parentDiv.insertBefore(newParagraph, paragraph1);
// insertAfter() does not exist, but there is a workaround using nextSibling
// example:
parentDiv.insertBefore(newNode, targetChildNode.nextSibling);
```
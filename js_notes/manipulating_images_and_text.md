# 52, 53 Manipulating images and text 
## with .className
- class can be replaced entirely by **className =**
```css
.hidden {display:none;}
```

```html
<img src="blobfish.jpg" id="ugly" onClick="makeInvisible();">
```

```js
function makeInvisible() {
    document.getElementById("ugly").className = "hidden";
}
```

- class name can be also added as a result of concatenation **+=** (including a space)
```js
function makeBig() {
    document.getElementById("p1").className += " big";
}
```

- parameter is another word for a variable used in functions to pass valuables

## with .src
- we can swap a source of an image with the .src attribute via JS
- a more common way is to assign an element to a variable first

```js
function swapPic(eId, newPic) {
    document.getElementById(eId).src = newPic;
}
```

```html
<img src="before-pic.jpg" id="before" onMouseover="swapPic('before','after-pic.jpg');">
```

## with .href
- winds up = ends up

```js
function getAddress() {
    const link = document.getElementById("link1");
    const address = link.href;
}
```


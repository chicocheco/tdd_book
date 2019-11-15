## 55 Setting styles via JS 

- there are plenty of attributes documented in docs that can modify CSS of identified elements
- we can modify styling, in addition to using css classes, directly like this

```js
function changeStyle() {
    document.getElementById("p1").style.fontSize = "2em";
    document.getElementById("p1").style.cssFloat = "left";
    document.getElementById("p1").style.visibility = "hidden";
    document.getElementById("p1").style.margin = "0 10px 0 10px";
}
```

- the following statement reads all the style properties, specified both in css and inline
```js
const m = document.getComputedStyle("mainPic").margin;
```
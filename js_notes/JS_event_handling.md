# Handling event within JS
- recommendable way of handling events in compare with in-line approach
 is from within JavaScript 
- event parameter (like `.onclick`) is always lowercase and assigned a function 
without quotes, with no following parentheses 

```html
<!--in-line event handling - old way-->
<input type="button" value="Click" onClick="sayHello();">

<!--event handling through id parameter -->
<input type="button" value="Click" id="button1">
<script>
function sayHello() {
    alert("Hi there.");
}

const b1 = document.getElementById("button1");
// watching for the element to be clicked right here:
b1.onclick = sayHello;  

// or more straightforward:
document.getElementById("button1").onclick = sayHello;
</script>
```
```js
// more event handlers
const targetImg = document.getElementById("i12");
targetImg.onmouseover = swapPic;

const emailFrm = document.getElementById("form5");
emailFrm.onsubmit = valEmail;
```
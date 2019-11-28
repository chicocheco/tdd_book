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
## jQuery equivalent
- this `document.getElementById("someId")` is replaced by a query `$(#"someId")`
- event handler `targetElement.onmouseover` is `.on("mouseover", ...`
- in pure JS we assign a named function for an event to an element(s) as in 
`target.onmouseover = namedFunction;` without calling to the function, no parentheses
- in jQuery we attach an event handler ANONYMOUS function for one or more events
 (separated by empty spaces) to the selected elements as in 
 `.on('keypress', function () { ... });`
- named function is like `function mySexyFunction(par1, par2) { ... )`
- anonymous function is like `function () { ... )` 

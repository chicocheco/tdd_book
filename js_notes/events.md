# 45, 46, 47, 48 Event handlers
## Link with onClick even handler
- in JS we use a term called an **event handler**
- the simplest event handler is a link 
- where # is there to only reload the current page, but it also scrolls up
- to avoid scrolling up we replace # for **"JavaScript:void(0)"**
- (from stackoverflow) we can also place **return false;** after whatever JS code in onClick
- inline method is not recommended to use, use function calls (scripting method)

Examples of inline event-handling (JS code as an attribute enclosed in ""):
```html
<a href="#" onClick="alert('Hi');">Click</a>
<a href="#" onClick="alert('Hi'); return false;">Click</a>
<a href="JavaScript:void(0)" onClick="alert('Hi');">Click</a>

<!--possible but not recommended usage -->
<a href="JavaScript:void(0)" onClick="let greet='hi'; alert(greet);">Click</a>
<!--onClick is not caseSensitive-->
```

## Button and picture with onClick even handler
Examples of inline even-handling
```html
<!--button (should be enclosed in form tags-->
<input type="button" value="Click" onClick="alert('Hello world!');">

<!--picture-->
<img src="button-greet.png" onClick="alert('Hello world!');">

<!--picture again but preferred approach-->
<img src="button-greet.png" onClick="greetTheUser();">
```

## onMouseover and onMouseout event handlers - when the user click in a field

Examples of onMouseover and onMouseout
- **onMouseover** - when we mouse over an element
- **onMouseout** - when we no longer mouse over an element (mostly used to return the state before)
```html
<!--change pic when the user mouses over and out (better to do this with CSS)-->
<img src="before-pic.jpg" onMouseover="src='after-pic.jpg'" onMouseout="src='before-pic.jpg'">
<!--display a message when the user mouses over-->
<h1 onMouseover="alert('Be sure to get your shopping done today.');">World Ends Tomorrow</h1>
<!--change the color of a link when the user mouses over, where a semicolon is needed (better with CSS)-->
<a href="index.html" onMouseover="this.style.color='green';">Home Page</a>
<!--expand the paragraph when the user mouses over-->
<p id="loris" onMouseover="expand();">Slow Loris: Mouse over for more info</p>
```

## onFocus and onBlur event handlers - when the user clicks in the field
- **onFocus** - when the user clicks into the field, it turns yellow
- **onBlur** - when she clicks out of the field, it reverts to white
```html
Email:<br>
<input type="text" size="30" 
onFocus="this.style.backgroundColor='yellow';" 
onBlur="this.style.backgroundColor='white';">

<!--more professional is to only call functions-->
Email:<br>
<input type="text" size="30" onFocus="makeFieldYellow();" onBlur="makeFieldWhite();">
```
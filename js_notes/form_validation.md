`# 82, 83, 84, 85, 86 Form validation
## Text fields
- prevent a form from being submitted by adding `return false;` at the end of 
the function as well as adding a matching keyword `return` in the calling code. 
When doing validating, we always add `return` to `onSubmit`
- we check that the user did not input any data by `.value.length === 0`
```html
<!--we could pass an ID as a parameter too, see drop-downs chapter-->
<form onSubmit="return checkForLastName();">
    Please enter your last name.<br>
    <input type="text" id="lastNameField">
    <input type="submit" value="Submit Form">
</form>
```
```js
function checkForLastName() {
    const targetField = document.getElementById("lastNameField");
    if (targetField.value.length === 0) {
        alert("Please enter your last name");
        targetField.focus(); // be user-friendly
        targetField.style.background = "yellow";
        return false; // this cancels the submission
    }
    targetField.style.background = "white";
}
```
## Drop-downs
- we check that the user did not select any option by `.selectedIndex === 0`
- here we pass an ID as a parameter, making the function reusable
```html
<form onSubmit="return checkForSelection('states');">
    <select id="states">
        <option value="" selected>SELECT A STATE</option>
        <option value="AL">Alabama</option>
        <option value="AK">Alaska</option>
        <option value="AZ">Arizona</option>
        <option value="AR">Arkansas</option>
        </select>&nbsp;&nbsp;
    <input type="submit" value="Submit Form">
</form>
```
```js
function checkForSelection(selecID) {
    const target = document.getElementById(selecID);
    if (target.selectedIndex === 0) {
        alert("Please select a state.");
        return false;
    }
}
```
## Radio buttons
- we check if a radio button is checked by `.checked` attribute
- to group the radio buttons we pass them a common `name` parameter, not id
- `id` parameter must be unique for each element, we cannot use it here
```html
<!--id must be unique, name can be shared-->
<form onSubmit="return validateRadios('r1');">
    <input type="radio" name="r1" value="cat"> Cat<br>
    <input type="radio" name="r1" value="bat"> Bat<br>
    <input type="radio" name="r1" value="hat"> Hat<br>
    <input type="submit" value="Submit Form">
</form>
```
```js
function validateRadios(eName) {
    const radios = document.getElementsByName(eName);
    for (let i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return true;
        }
    }
    alert("Please check one.");
    return false;
}
```
## ZIP codes
- HTML allows to keep the user from entering too many digits by `maxlength=5`
- but we have to use JS for the minimum length of digits
- to find out whether converting via `parseInt()` to digits worked we use `isNaN()`
to answer the question "is Not a Number?"
- more elegant way is to use regex
```js
function validateZIP() {
    const valueEntered = document.getElementById("zip").value;
    const numChars = valueEntered.value.length;
    if (numChars < 5) {
        alert("Please enter a 5-digit code.");
        return false;
    }
    for (let i = 0; i < 5; i++) {
    const thisChar = parseInt(valueEntered[i]);  // attempt to convert
    if (isNaN(thisChar)) {  // isNaN stands for "is Not a Number"
        alert("Please enter only numbers.");
        return false;  // cancel the submission
    }
    }
}
```
## Email address
- remember that if `.indexOf(char)` returns anything else than -1, it is present
- if we don't wanna use regex we can test for index/position of particular chars
- email address looks someting like this: <one char>@<one char>.<two chars>
- we can tell the position of a character by its index in the string
```js
function validateEmail() {
    let addressIsLegal = true;
    const eEntered = document.getElementById("address").value;
    if (eEntered.indexOf(" ") !== -1) {
        addressIsLegal = false;
    }
    if (eEntered.indexOf("@") < 1 || eEntered.indexOf("@") > eEntered.length - 5) {>
        addressIsLegal = false;
    }
    if (eEntered.indexOf(".") - eEntered.indexOf("@") < 2 ||
        eEntered.indexOf(".") > eEntered.length - 3) {  // at least 3 characters after a do
        addressIsLegal = false;
    }
    if (addressIsLegal === false) {
        alert("Please correct email address");
        return false;
    }
}
```
- better alternative is to use a **regular expression** that expresses a pattern
- `*` wildcard operator
```js
function validateEmail() {
    const eEntered = document.getElementById("address").value;
    const emailCorrectPattern = /^[\w\-\.\+]+\@[a-zA-Z0-9\. \-]+\.[a-zA-z0-9]{2,4}$/;
    if (!(eEntered.match(emailCorrectPattern))) {
        alert("Please correct email address");
        return false;
    }
}
```
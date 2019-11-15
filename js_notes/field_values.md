# 49 Reading field values
## onSubmit event handler
- we place the **onSubmit** event handler to the <form> tag and not to the button
- onSubmit can be used to validate entered form data, fields are identified by their IDs
- we read the current input value (before sending to the server) by **document.getElementById(<nameOfField>).value**

```js
function checkAddress(fieldId) {
    if (document.getElementById(fieldId).value === "") {
        alert("Email address required.");
    }
}
```
```html
<!--we use a JS function from above-->
<form onSubmit="checkAddress('email');">
Email:
<input type="text" id="email">
<input type="submit" value="Submit">
</form>
```

- writing text to a field is very simple, assigning with "="
```js
function fillCity() {
    let cityName;   
    let zipEntered = document.getElementById("zip").value;
    switch (zipEntered) {
    case "60608" :
        cityName = "Chicago";
        break;
    case "68114" :
        cityName = "Omaha";
        break;
    case "53212" :
        cityName = "Milwaukee";
  }
  document.getElementById("city").value = cityName;
}
```
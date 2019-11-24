# 87, 88 Exceptions
## try and catch
- when we want to know what got broken we have to catch the error with try...catch
- the error message is assigned to `err` variable by convenience
- keywords `try` and `catch` are always paired
- in Python we use try...except block
```js
function greetWorld() {
    try {
        const greeting = "Hello world!";
        aler(greeting);
    }
    catch(err) {
        alert(err);
    }
}

greetWorld();
```

## throw to define your own error in try...catch
- in Python the equivalent is `raise`
- throw pass a value or variable to a parameter (parameter passed to catch)
```html
<form onSubmit="return checkPassword();">
    Enter a password<br>
    (8-12 characters, at least 1 number, no spaces)<br>
    <input type="text" id="f1">
    <input type="submit" value="Submit">
</form>

<script>
function checkPassword() {
    try {
        const pass = document.getElementById("f1").value;
        if (pass.length < 8) {
            throw "Please enter at least 8 characters.";
        }
        if (pass.indexOf(" ") !== -1) {
            throw "No spaces in the password, please.";
        }
        let numberSomewhere = false;
        for (let i = 0; i < pass.length; i++) {
            if (isNaN(pass(i, i+1)) === false) {
            numberSomewhere = true;
            break;
            }
        }
        if (numberSomewhere === false) {
            throw "Include at least 1 number.";
        }
    }
    catch(err) {
        alert(err);
    }
}
</script>
```
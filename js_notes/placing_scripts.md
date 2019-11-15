# Placing JS scripts

- generally the best place for scripts is at the end of the body section of HTML
- JS code must be enclosed between <script> tags
```html
<script>
function sayHi() {
    alert("Hello world!");
}
function sayBye() {
    alert("Buh-bye!");
}
</script>
```
- JS code can be also in a JavaScript file .js
```html
<script src="whatever.js"></script>
```
# 51 Modifying inner HTML with JS
## Paragraph expanding function
- the attribute **.innerHTML** can change anything within the identified HTML element like <p>
- the HTML **<em>** element marks text that has stress emphasis but is not the same as **<i>** which does NOT emphasize

```js
// single backtics for long strings `` in JS
function expandLoris() {
    let expandedParagraph = `Slow lorises are a group of several species of trepsirrhine primates which make up the genus
    Nycticebus. They have a round head, narrow snout, large eyes, and a variety of distinctive coloration patterns that
    are species-dependent. The hands and feet of slow lorises have several adaptations that give them a pincer-like grip
    and enable them to grasp branches for long periods of time. Slow lorises have a toxic bite, a rare trait among
    mammals.`;
    document.getElementById("slowLoris").innerHTML = expandedParagraph;
}
```

```html
<p id="slowLoris">
Slow lorises are a group of several species of strepsirrhine primates which make up the genus Nycticebus.
<a href="javascript:void(0);" onClick="expandLoris();"><em>Click for more.</em></a>
<!--alternatively?-->
<a href="#" onClick="expandLoris(); return false;"><em>Click for more.</em></a>
</p>
```
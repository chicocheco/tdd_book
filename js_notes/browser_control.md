# 76, 77, 78, 79, 80, 81 Browser control

We can read the current URL from the browser
```js
// complete URL or "document.URL" or "window.location" or "location"
const whereWeAt = window.location.href;

// domain name, the base, the root
const theDomain = window.location.hostname;

// the path (homepage would return "/")
const thePath = window.location.pathname;

// identify an anchor (#) if exists, else ""
// as "guarantee" in "http://www.me.com/lojack.html#guarantee"
const theAnchor = window.location.hash

// "window" can be omitted in them
```
We can also assign a new URL and redirect the browser to it
```js
// redirect
window.location.href = "http://www.seznam.cz";
window.location = "http://www.seznam.cz";
location = "http://www.seznam.cz";

const currentSite = window.location.hostname;
const destination = "http://" + currentSite + "/wow.html";
window.location.href = destination;

// keep history (back button works)
window.location.assign("http://www.seznam.cz");
// don't keep history
window.location.replace("http://www.seznam.cz");

// reloading
window.location.reload(true); // reload from the server
window.location.reload(false); // reload from the cache
window.location.reload(); // reload from the cache
```
## Forward and reverse
These commands are possible only if there is where to go (in history)
```js
// going back as if clicking on the button
history.back();

// going forward
history.forward();
 
// equivalent of pressing backspace 3x or alt-right arrow 2x
history.go(-3);
history.go(2);

// referrer - if the user clicked a link to get to the current page, we can get
// the URL of the page where the link was clicked
const whereUserCameFrom = document.referrer;
```
## Filling the window with content
- open a new window by `windows.open()`
- place HTML string by `document.write()` method, it clobbers all existing content
```js
// open a new window/tab of full size (depends on the browser)
const monkeyWindow = window.open();
const windowContent = `<h1>Capuchin monkey</h1><img src= 'monkey.jpg'><p>The word capuchin
 derives from a group of friars<br>named the Order of Friars Minor Capuchin who wear<br>brown
robes with large hoods covering their heads.</p>`;

// write in it some HTML code
monkeyWindow.document.write(windowContent);

// or we can assign a document to the windows
monkeyWindow.location.assign("http://www.animals.com/capuchin.html");
monkeyWindow.location.href = "http://www.animals.com/capuchin.html";

// or we can directly open a new window with this URL
const monkeyWindow2 = window.open("http://www.animals.com/capuchin.html");

// if on the same domain, then
const monkeyWindow3 = window.open("capuchin.html");

// close it
monkeyWindow3.close();
```
## Controlling the window's size and location
- second positional parameter of `window.open()` is a name to specify the target
 attribute of `<a>` or `<form>`
- third parameter is defining size and position of a window enclosed in a 
single pair of quotes with no spaces and the order does not matter
- width and height must be a minimum of 100
```js
const monkeyWindow = window.open("https://www.seznam.cz/", "win1", "width=420,height=380,left=200,top=100");

// alternatively
const windowSpecs = "'faq.html', 'faq', 'width=420,height=380,left=200,top=100'";
const faqPage = window.open(windowSpecs);
```
## Testing for popup blockers
We can open and and quickly close to see if the handle will have a value, else
it is `null` therefore it was blocked
```js
function checkForPopBlocker() {
    // size+loc parameter must be on a third position (leaving first two empty)
    // testProp is the "handle"
    // in IE it would be assigned undefined instead of null
    const testPop = window.open("", "","width=100,height=100");
    if (testPop === null || typeof(testPop) === "undefined") {
        alert("Please disable your popup blocker.");
    }
    testPop.close();
}
```
# 31, 32, 33, 34 Date object

- we get the date and time objects in JS like by **new Date();**
- this objects has various methods like **.getDay** that returns 0 to 6
- Date() can be converted to a string same as numbers by **.toString()**

```js
// taking advantage 0-based indices of arrays to get the name of current day
// in JS a week starts with Sunday = 0
dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
now = new Date();
theDay = now.getDay();
nameOfToday = dayNames[theDay];
```
To do this in Python
```python
# in Python a week starts with Monday (0-based) with .weekday()
# or 1-based with .isoweekday()
import datetime
now = datetime.datetime.now()
day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
the_day = now.weekday()
name_of_today = day_names[the_day]
```

## Date() object of future
- the epoch is the point where the time starts, and is platform dependent
- for Unix, the epoch is January 1, 1970, 00:00:00 (UTC)
- in JS we get milliseconds after the epoch by **new Date().getTime()** 
- in Python we get seconds after the epoch by **time.time()**
```js
const today = new Date();
const doomsday = new Date("June 30, 2035");
const msToday = today.getTime();
const msDoomsday = doomsday.getTime();
const msDiff = msDoomsday - msToday;
// convert milliseconds to days and round down to whole days
const dDiff = Math.floor(msDiff / (1000 * 60 * 60 * 24));
// divide by 1000 to convert to seconds
// divide by (1000 * 60) to convert to minutes
// divide by (1000 * 60 * 60) convert to hours
// divide by (1000 * 60 * 60 * 24) convert to days
alert(dDiff);
```

## Time in milliseconds that elapsed between the reference date and the beginning of 1980.
```js
alert(new Date("January 1, 1980").getTime());
```

## Setting, modifying Date objects
- we can also change any part of a Date object with .setMonth(6) - July, etc.
- notice that January is 0, not 1
- the methods are:
 - .setFullYear()
 - .setMilliseconds()

- one seconds has 1000 milliseconds
```js
// this creates a Date object of the current moment
const d = new Date();
// and this is how we keep it all the same except for the year
d.setFullYear(2001);
const onlyYear = d.getFullYear();
alert(onlyYear);
```
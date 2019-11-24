# 69, 70, 71, 72, 73, 74, 75 Objects

- objects with no methods in JS are similar to dictionaries or data classes in Python
- objects with methods are like classes in Python 
- **properties** is are accessed by [key] or a dot notation `.key` (not in Python)
- property is a **variable** that is attached to an object
- method is a **function** that is attached to an object
- because we started with `=` we finish with `;`
```js
// one-off literal object definition (not constructor)
const plan1 = {
    name: "Basic",
    price: 3.99,
    space: 100,
    transfer: 1000,
    pages: 10
};

// MyVar is an empty variable, it is "undefined"
// myObj is an an empty object
// const variable without initializer is not allowed
let myVar;
const myVar2;
const myObj = {};

// delete a property
delete deal3.market;

// membership test with "in" keyword returns either false or true
propertyExists = "market" in deal3;
```

## Methods of an object and keyword this
- a function attached to an object is known as a **method**
- the same way we define a method of a class in Python we can define an object's method
- to refer to properties in a method of the same object we use a keyword `this.`
- the equivalent of `this` in Python is `self` (in classes)
- defining methods of objects is like defining another property using colon (:)
- every property or method, except the last one, is separated by comma (,)
- a method definition starts with its name followed by colon and a keyword `function`
- a function definition start with a keyword `function` followed by its name (the opposite order)
```js
// one-off literal object definition (not constructor)
const plan1 = {
    name: "Basic",  // separate with a comma
    price: 3.99,
    space: 100,
    transfer: 1000,
    pages: 10,
    discountMonths: [6, 7],
    calcAnnual: function(percentIfDisc) {  // notice that the order is the opposite to declaring a function
        let bestPrice = this.price;  // same as plan1.price
        const currDate = new Date();
        const thisMo = currDate.getMonth(); // returns a digit
        for (let i = 0; i < this.discountMonths.length; i++) {
            if (this.discountMonths[i] === thisMo) {
                bestPrice = this.price * percentIfDisc;
                break;
            }
        }
        return bestPrice * 12;
    }  // no need a comma at the end
};

// the calling statement for 15% discount when paying in discount months
const annualPrice = plan1.calcAnnual(0.85);
```

## Constructors
- constructor is like a factory that is called a construction function
- constructors create objects
- its name is Capitalized by convenience to distinguish it from a reg. function 
- keyword `this` is replaced by the object name when the function executes
- to create a new object we add `new` in the calling code
- without the `new ` keyword it would be just a regular function call
```js
// constructor function or simply a constructor
function Plan(name, price, space, transfer, pages) {
    this.name = name;  // what starts with "=", finished with ";"
    this.price = price;
    this.space = space;
    this.transfer = transfer;
    this.pages = pages;
}

const plan1 = new Plan("Basic", 3.99, 100, 1000, 10);
// so plan1.price; returns a value passed in a parameter price  3.99
const plan2 = new Plan("Premium", 5.99, 500, 5000, 50);
const plan3 = new Plan("Ultimate", 9.99, 2000, 20000, 500);

// names of properties can differ from names of parameters
function PlanDifferent(name, price, space, transfer, pages) {
    this.doc = name;
    this.grumpy = price;
    this.sleepy = space;
    this.bashful = transfer;
    this.sneezy = pages;
}
```

## Constructors for methods
- to have the same method in several objects we can include it its constructor
```js
// constructor function or simply a constructor including a method
function Plan(name, price, space, transfer, pages, discountMonths) {
    this.name = name;
    this.price = price;
    this.space = space;
    this.transfer = transfer;
    this.pages = pages;
    this.discountMonths = discountMonths;
    this.calcAnnual = function(percentIfDisc) {
        let bestPrice = this.price;
        const currDate = new Date();
        const thisMo = currDate.getMonth();
        for (let i = 0; i < this.discountMonths.length; i++) {
            if (this.discountMonths[i] === thisMo) {
                bestPrice = this.price * percentIfDisc;
                break;
            }
        }
        return bestPrice * 12;
    };
}
// create three new objects (here 3 hosting plans)
// each with 6 properties and 1 method
// the method calcAnnual gets copied to each object
const p1 = new Plan("Basic", 3.99, 100, 1000, 10, [6, 7]);
const p2 = new Plan("Premium", 5.99, 500, 5000, 50, [6, 7, 11]);
const p3 = new Plan("Ultimate", 9.99, 2000, 20000, 500, [6, 7]);

// but to calculate the annual price we must pass a parameter to an object
const annualPrice = p2.calcAnnual(.85);  // 15% discount for a year
```
- notice that in the one-off literal object definition (no constructor),
we define a method with a semicolon `CalcAnnual: function(percentIfDisc) {`
 and if not at the end, separate with a comma
- within a constructor, we define a method with an equal sign like
`this.calcAnnual = function(percentIfDisc) {` finishing always with a semicolon

## Prototypes
- when we want every particular object inherit the same variable or a method,
we declare it with a `prototype` keyword apart

```js
// use a keyword "prototype" to attach the method to every new object
// based on a constructor function named "Plan"

// it's identical to the one placed directly in the constructor
// except for the keyword "prototype"
Plan.prototype.calcAnnual = function(percentIfDisc) {
    let bestPrice = this.price;
    const currDate = new Date();
    const thisMo = currDate.getMonth();
    for (let i = 0; i < this.discountMonths.length; i++) {
        if (this.discountMonths[i] === thisMo) {
            bestPrice = this.price * percentIfDisc;
            break;
        }
        }
    return bestPrice * 12;
};

// we can still override a prototype when exceptions occur
Plan.prototype.cancellable = true;
const p1 = new Plan("Basic", 3.99, 100, 1000, 10, [6, 7]);
p1.cancellable = false;

// to get a parameter "msg" by the constructor not the call statement
Object1.prototype.method1 = function() {
  alert(this.msg);
};
```

## Checking for properties and methods
- find out whether an objects has a particular property or not write a statement
like this `const gotTheProp = "price" in plan1;`
- when using `in` keyword, we get `true` or `false`
- we can also write **membership tests** for methods
- `in` keyword tests even for inherited properties and methods (from prototypes) 
but if we want to test only for explicitly declared properties we use `.hasOwnProperty()` 
```js
// membership test, property name always enclosed in quotes
const gotTheProp = "price" in plan1;

// make a list of an object's properties (inherited included)
// this for loop iterates until there is not more properties to enumerate 
let listOfProperties = [];
for (let prop in plan1) {
    listOfProperties.push(prop);
}

// make a list only of non-inherited properties
let listOfProperties = [];
for (let prop in plan1) {
    if (plan1.hasOwnProperty(prop)) {
        listOfProperties.push(prop);
    }
}

// we can test a literal property as well
const isOwnedProperty = plan1.hasOwnProperty("price");

// notice that there is another kind of foor loop, compare these two
for (let i = 0; i < listOfProperties.length; i++) {
	listOfProperties[i] = listOfProperties[i] + "XYZ";
}

// this does the same thing, it's called for/in loop
for (let ele in listOfProperties) {
	listOfProperties[ele] = listOfProperties[ele] + "ABC";
}
```

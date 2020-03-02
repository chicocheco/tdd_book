# Properties in Python explained

Properties are a special kind of attribute. Basically, when Python encounters the following code:

```
spam = SomeObject()
print(spam.eggs)
```

it looks up `eggs` in `spam`, and then examines `eggs` to see if it has a `__get__`, `__set__`, or `__delete__` method 
— if it does, it's a **property**. If it is a **property**, instead of just returning the eggs object 
(as it would for any other attribute) it will call the `__get__` method (since we were doing lookup) 
and return whatever that method returns.

```python
class A(object):
    _x = 0
    '''A._x is an attribute'''

    @property
    def x(self):
        """
        A.x is a property
        This is the getter method
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._x = value
```
```
>>> a = A()
>>> a._x = -1
>>> a.x = -1
Traceback (most recent call last):
  File "ex.py", line 15, in <module>
    a.x = -1
  File "ex.py", line 9, in x
    raise ValueError("Must be >= 0")
ValueError: Must be >= 0
```

## From the official docs

A property object has getter, setter, and deleter methods usable as decorators that create a copy of the property 
with the corresponding accessor function set to the decorated function. This is best explained with an example:

```python
# Without decorators:
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```

If `c` is an instance of `C`, 
`c.x` will invoke the getter, (corresponding to @property)
`c.x = value` will invoke the setter and (corresponding to @x.setter)
`del c.x` the deleter. (corresponding to @x.deleter)

```python
class C:
    def __init__(self):
        self._x = None  # attribute
    
    # 1 property, 3 methods, 3 decorators
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter  # setter of 'x'
    def x(self, value):
        self._x = value

    @x.deleter  # deleter of 'x'
    def x(self):
        del self._x
```

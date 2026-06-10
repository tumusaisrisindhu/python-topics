# Day 2 Notes - Decorators

## What is a Decorator?

A decorator is a function that adds extra functionality to another function without changing its original code.

---

## Basic Syntax

```python
@decorator
def greet():
    print("Hello")
```

Equivalent to:

```python
greet = decorator(greet)
```

---

## Structure of a Decorator

```python
def decorator(func):

    def wrapper():

        # Extra functionality

        func()

    return wrapper
```

---

## Why Use Decorators?

To avoid repeating code.

Examples:

- Logging
- Authentication
- Timing
- Validation
- Caching

---

## Nested Functions

Functions inside another function.

```python
def outer():

    def inner():
        print("Hello")
```

---

## Wrapper Function

A function that runs before and after the original function.

```python
def wrapper():

    print("Before")

    func()

    print("After")
```

---

## \*args and \*\*kwargs

Used so decorators work with any function.

```python
def wrapper(*args, **kwargs):
```

---

## Decorator With Arguments

```python
@repeat(3)
```

Requires three layers:

```python
def repeat(times):

    def decorator(func):

        def wrapper():

            pass

        return wrapper

    return decorator
```

---

## Multiple Decorators

```python
@A
@B
def func():
```

Python executes:

```python
func = A(B(func))
```

Bottom decorator runs first.

---

## Common Interview Questions

1. What is a decorator?
2. Why use decorators?
3. What is a wrapper?
4. Why use \*args and \*\*kwargs?
5. What is a nested function?
6. How do decorators work internally?
7. What are decorators with arguments?
8. Explain multiple decorators.

---

## Real World Uses

- Flask Routes
- Django Authentication
- API Logging
- Execution Timing
- Caching
- Rate Limiting

---

## Revision Shortcut

Decorator = Function that wraps another function.

Flow:

Function
↓
Decorator
↓
Wrapper
↓
Extra Functionality
↓
Original Function

# Memory Management

## Concepts

- Mutable vs Immutable
- Shallow Copy
- Deep Copy
- Reference Counting
- Garbage Collection

---

# Mutable Objects

Objects that can be modified after creation.

Examples:

- list
- dict
- set

```python
numbers = [1, 2, 3]
numbers.append(4)
```

Same object is modified.

---

# Immutable Objects

Objects that cannot be modified after creation.

Examples:

- int
- float
- str
- tuple
- bool

```python
name = "Python"
name = name + " Developer"
```

A new object is created.

---

# Mutable vs Immutable

```python
a = [1, 2]
b = a

a.append(3)

print(b)
```

Output

```python
[1, 2, 3]
```

Both variables reference the same object.

---

# Shallow Copy

Creates a new outer object.

Nested objects are still shared.

```python
import copy

data = [[1, 2], [3, 4]]

new_data = copy.copy(data)
```

Changes inside nested objects affect both.

---

# Deep Copy

Creates completely independent copies.

```python
import copy

data = [[1, 2], [3, 4]]

new_data = copy.deepcopy(data)
```

Changes do not affect original.

---

# Reference Counting

Python keeps track of how many variables reference an object.

```python
x = [1, 2]
y = x
```

Reference count increases.

When count becomes zero, memory is released.

---

# Garbage Collection

Handles circular references.

```python
a = []
b = []

a.append(b)
b.append(a)
```

Python's Garbage Collector removes unreachable objects.

```python
import gc

gc.collect()
```

---

# Important Functions

## id()

Returns memory address.

```python
x = [1, 2]

print(id(x))
```

---

## is

Checks object identity.

```python
a is b
```

---

## ==

Checks value equality.

```python
a == b
```

---

# Interview Questions

### Difference between == and is

- == compares values
- is compares memory addresses

---

### Difference between assignment and copy

```python
b = a
```

Same object.

```python
b = copy.copy(a)
```

New outer object.

---

### Difference between shallow and deep copy

Shallow Copy

- Copies outer object only

Deep Copy

- Copies everything recursively

---

# Quick Revision

Mutable

- list
- dict
- set

Immutable

- int
- float
- str
- tuple
- bool

copy.copy()

- shallow copy

copy.deepcopy()

- deep copy

id()

- memory address

is

- identity comparison

==

- value comparison

gc.collect()

- run garbage collector

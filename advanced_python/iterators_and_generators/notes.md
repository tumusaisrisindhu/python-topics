# Iterators & Generators

## Concepts

### Iterable

An object that can be iterated over.

Examples:

- list
- tuple
- string
- set
- dictionary

```python
nums = [1, 2, 3]
for num in nums:
    print(num)
```

### Iterator

An object that remembers its state and returns one item at a time.

Methods:

- **iter**()
- **next**()

```python
nums = [1, 2, 3]

it = iter(nums)

print(next(it))
print(next(it))
```

### iter()

Converts an iterable into an iterator.

```python
nums = [1, 2, 3]
it = iter(nums)
```

### next()

Returns the next value from an iterator.

```python
print(next(it))
```

Raises:

```python
StopIteration
```

---

## Custom Iterator

Requirements:

- **iter**()
- **next**()

```python
class Counter:

    def __init__(self, end):
        self.current = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value
```

Use when:

- Pagination
- Streaming data
- Custom sequences

---

## Generators

Functions that use `yield`.

Benefits:

- Memory efficient
- Lazy evaluation
- Easier than custom iterators

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

---

## yield vs return

| yield                      | return                   |
| -------------------------- | ------------------------ |
| Pauses function            | Ends function            |
| Produces values one by one | Produces one final value |
| Memory efficient           | Stores complete result   |

Example:

```python
def gen():
    yield 1
    yield 2
```

---

## Generator Expression

List Comprehension:

```python
squares = [x*x for x in range(10)]
```

Generator Expression:

```python
squares = (x*x for x in range(10))
```

Preferred for:

- Large datasets
- Streaming data

---

## Lazy Evaluation

Values are generated only when needed.

```python
gen = (x*x for x in range(1000000))

print(next(gen))
```

Advantage:

- Low memory usage

---

## Common Generator Examples

### Fibonacci Generator

```python
def fibonacci():

    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b
```

### Infinite Counter

```python
def counter():

    num = 1

    while True:
        yield num
        num += 1
```

---

## Iterator vs Iterable

| Iterable            | Iterator                   |
| ------------------- | -------------------------- |
| Can be looped over  | Produces values one by one |
| Uses iter()         | Uses next()                |
| list, tuple, string | Result of iter()           |

Example:

```python
nums = [1, 2, 3]

it = iter(nums)
```

nums → Iterable

it → Iterator

---

## Iterator vs Generator

| Iterator                       | Generator                |
| ------------------------------ | ------------------------ |
| Uses class                     | Uses function            |
| **iter** and **next** required | yield required           |
| More code                      | Less code                |
| Manual implementation          | Automatic implementation |

---

## Internal Working of for Loop

```python
for x in nums:
    print(x)
```

Internally:

```python
it = iter(nums)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

---

## Real-World Use Cases

### Iterators

- Database pagination
- Sensor data
- API responses
- Custom collections

### Generators

- Log file processing
- CSV processing
- Streaming APIs
- Large datasets
- Background jobs

---

## Mini Project

### Log File Streaming Reader

Goal:

- Read large log files line-by-line
- Avoid loading entire file into memory

Concepts Used:

- Generator
- yield
- File handling

```python
def read_logs(file_path):

    with open(file_path) as file:
        for line in file:
            yield line.strip()
```

Possible Enhancements:

- Count ERROR logs
- Search keyword
- Real-time monitoring
- Export filtered logs

---

## Interview Questions

### Basic

1. What is an iterable?
   An object that can be iterated over.

2. What is an iterator?
   An object that remembers its state and returns one item at a time
3. Difference between iter() and next()?
   | iter() | next() |
   | ---------------------------- | ---------------------- |
   | Creates an iterator | Gets the next value |
   | Called once usually | Called repeatedly |
   | Converts iterable → iterator | Moves iterator forward |

4. What is StopIteration?
   It is an exception raised when there are no more items left in an iterator.
5. What is a generator?
   A generator is a special function that produces values one at a time using yield.

### Intermediate

6. Difference between iterator and generator?
   | Iterator | Generator |
   | ----------------------------------- | ------------------------ |
   | Created using class | Created using function |
   | Needs `__iter__()` and `__next__()` | Uses `yield` |
   | More code | Less code |
   | Manual implementation | Automatic implementation |

7. Difference between yield and return?
   | yield | return |
   | --------------------------- | ------------------------ |
   | Pauses function | Ends function |
   | Returns one value at a time | Returns all at once |
   | Used in generators | Used in normal functions |

8. Why are generators memory efficient?
   Generators create values only when needed, instead of storing everything in memory.

   def numbers():
   for i in range(1000000):
   yield i

   Only one value exists at a time.

9. How does a for loop work internally?
   A for loop automatically uses iter() and next().

   for item in data:
   print(item)

Internally:

    it = iter(data)

    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break

10. What is lazy evaluation?
    Lazy evaluation means values are generated only when needed, not all at once.

    Generators use lazy evaluation.

    def numbers():
    yield 1
    yield 2

    The values are created only when next() is called.

### Advanced

11. Create a custom iterator.
    class Count:
    def **init**(self, max_num):
    self.max_num = max_num
    self.current = 1

        def **iter**(self):
          return self

        def **next**(self):
          if self.current > self.max_num:
          raise StopIteration

          value = self.current
          self.current += 1
          return value

    for num in Count(5):
    print(num)

12. Create a Fibonacci generator.
    def fibonacci(n):
    a, b = 0, 1

    for \_ in range(n):
    yield a
    a, b = b, a + b
    for num in fibonacci(5):
    print(num)

Output:

0
1
1
2
3

13. Create an infinite generator.
    def infinite():
    num = 1

    while True:
    yield num
    num += 1

    Usage:

    gen = infinite()

    print(next(gen))
    print(next(gen))
    print(next(gen))

14. When would you choose a generator over a list?
    Use a generator when:

    Working with large data
    Reading huge files
    Processing API responses
    Memory optimization is important
    Data is produced one item at a time

    Example:

    # Better

    (i for i in range(1000000))

    # Uses more memory

    [i for i in range(1000000)]

15. Explain real-world use cases of generators.
    1. Reading large log files
       def read_logs(file):
       for line in file:
       yield line

    Reads one line at a time. 2. Streaming API data
    def fetch_data():
    while True:
    yield get_next_record()

    Processes data continuously. 3. Pagination
    def pages():
    yield page1
    yield page2

    Loads pages only when needed. 4. Data pipelines
    filtered = (x for x in data if x > 10)

    Processes data step by step.

---

## Revision Checklist

- [ ] Iterable vs Iterator
- [ ] iter()
- [ ] next()
- [ ] StopIteration
- [ ] Custom Iterator
- [ ] Generator
- [ ] yield
- [ ] Generator Expression
- [ ] Lazy Evaluation
- [ ] Iterator vs Generator
- [ ] Fibonacci Generator
- [ ] Infinite Counter
- [ ] Log Streaming Project

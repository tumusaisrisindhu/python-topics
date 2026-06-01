# Object Copy Simulator

A mini project built while learning:

- Mutable vs Immutable Objects
- Shallow Copy
- Deep Copy
- Memory Management
- Object References
- id() Function

---

## Features

- Demonstrates Assignment
- Demonstrates Shallow Copy
- Demonstrates Deep Copy
- Displays Memory IDs
- Shows how changes affect copied objects

---

## Project Structure

```text
mini_project_object_copy_simulator/
│
├── app.py
├── copy_simulator.py
└── README.md
```

---

## Run

```bash
python app.py
```

---

## Concepts Used

### Assignment

```python
assigned = original
```

Both variables point to the same object.

---

### Shallow Copy

```python
copy.copy(original)
```

Creates a new outer object.

Nested objects remain shared.

---

### Deep Copy

```python
copy.deepcopy(original)
```

Creates completely independent copies.

---

### id()

```python
id(object)
```

Returns object's memory address.

---

## Learning Outcome

After completing this project you will understand:

- How Python stores objects in memory
- Difference between assignment and copying
- Difference between shallow and deep copy
- How object references work
- Why memory IDs matter

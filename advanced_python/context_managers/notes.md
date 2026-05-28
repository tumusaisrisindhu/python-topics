# Context Managers

## Concepts

- with statement
- **enter**()
- **exit**()
- Resource management
- Custom context managers

## Why Context Managers?

Used to automatically clean up resources.

Examples:

- Files
- Database connections
- Network connections
- Locks

## Syntax

```python
with open("file.txt") as f:
    data = f.read()
```

## interview quetions

1: Why use context managers?
A: To automatically acquire and release resources, ensuring proper cleanup even if exceptions occur.

2: What methods are required for a context manager class?
A: **enter**() and **exit**().

3: What happens if an exception occurs inside a with block?
A: **exit**() is still executed, resources are cleaned up, and the exception is re-raised unless handled.

4: Difference between a module and package?
A: A module is a single .py file, while a package is a directory containing multiple modules.

5: Difference between import module and from module import func?
A: import module imports the entire module and requires module.func(), while from module import func imports only the specified function for direct use.

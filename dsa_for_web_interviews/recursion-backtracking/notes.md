# Recursion & Backtracking

# What is Recursion?

Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

Instead of solving the whole problem at once, recursion breaks it into smaller problems until it reaches a stopping condition called the **Base Case**.

---

## Real World Example

Imagine standing between two mirrors.

Mirror → Mirror → Mirror → Mirror ...

The reflection keeps repeating.

Similarly, in recursion, a function keeps calling itself until it reaches a stopping condition.

Another example:

Imagine opening a set of nested gift boxes.

Box 1
 └── Box 2
      └── Box 3
           └── Small Gift 🎁

You keep opening smaller boxes until there are no more boxes.

Then you close them one by one.

Recursion works exactly like this.

---

# Structure of a Recursive Function

Every recursive function has two parts.

1. Base Case
2. Recursive Case

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

Base Case

```python
if n == 0:
    return
```

Recursive Case

```python
countdown(n - 1)
```

Without a base case, recursion never stops.

---

# Base Case

The condition where recursion stops.

Example

```python
if n == 0:
    return
```

Think of it as reaching the destination.

---

# Recursive Case

The part where the function calls itself with a smaller input.

Example

```python
factorial(n)
↓

factorial(n-1)
```

Each recursive call should move closer to the base case.

---

# Call Stack

Python keeps track of function calls using a Stack.

Every function call is pushed onto the stack.

When a function finishes,
it is popped from the stack.

Example

```python
factorial(3)

↓

factorial(2)

↓

factorial(1)

↓

factorial(0)
```

Then it returns

```
factorial(0)

↑

factorial(1)

↑

factorial(2)

↑

factorial(3)
```

Think of a stack of plates.

Last plate placed
↓

First plate removed

LIFO
(Last In First Out)

---

# Recursion Tree

A Recursion Tree shows every recursive function call.

Example

```python
def fun(n):
    if n == 0:
        return

    fun(n-1)
```

For

```
fun(3)
```

Tree

```
fun(3)
 |
fun(2)
 |
fun(1)
 |
fun(0)
```

Example 2

Fibonacci

```
fib(4)

        4
      /   \
     3     2
    / \   / \
   2   1 1   0
  / \
 1   0
```

Recursion trees help us understand

- Number of function calls
- Time Complexity
- Duplicate work

---

# Why Use Recursion?

Useful when problems naturally break into smaller versions.

Examples

✔ Tree Traversal

✔ Graph DFS

✔ Binary Search

✔ Merge Sort

✔ Quick Sort

✔ Maze Solving

✔ Sudoku Solver

✔ Folder Traversal

---

# Advantages

✔ Cleaner code

✔ Easy to solve tree problems

✔ Good for divide-and-conquer

✔ Elegant solutions

---

# Disadvantages

✔ More memory usage

✔ Function call overhead

✔ Can cause Stack Overflow

✔ Sometimes slower than loops

---

# Recursion vs Iteration

Recursion

- Uses function calls
- Uses Call Stack
- Easier for tree problems
- More memory

Iteration

- Uses loops
- No extra stack
- Faster
- Less memory

---

# What is Backtracking?

Backtracking is an advanced form of recursion.

It tries one choice.

If that choice doesn't work,

it goes back,

undoes the choice,

and tries another one.

Think of

Try

↓

Check

↓

Wrong?

↓

Undo

↓

Try another

---

## Real World Example

Imagine solving a maze.

You choose one path.

If it's blocked,

you return to the previous point

and choose another path.

Exactly how backtracking works.

---

# Steps of Backtracking

1. Choose
2. Explore
3. Undo (Backtrack)

Template

```python
def backtrack():
    if solution_found:
        print(answer)
        return

    for choice in choices:

        make_choice()

        backtrack()

        undo_choice()
```

Notice the last step.

Undoing is what makes it backtracking.

---

# When is Backtracking Used?

Sudoku Solver

N Queens

Maze Solver

Word Search

Permutations

Subsets

Combination Sum

Palindrome Partitioning

Rat in Maze

Crossword Puzzle

---

# What are Subsets?

A subset is any possible selection of elements.

For

```
[1,2]
```

Subsets

```
[]

[1]

[2]

[1,2]
```

Total subsets

```
2^n
```

where

n = number of elements

Example

```
3 elements

2³ = 8 subsets
```

---

# Recursion Idea Behind Subsets

For every element,

there are only two choices.

Include it

or

Don't include it

Example

```
1 2

Take 1

Skip 1

Take 2

Skip 2
```

Decision Tree

```
          []
       /      \
     1          x
   /   \      /   \
 12   1      2    []
```

---

# What are Permutations?

Permutation means arranging elements in every possible order.

Example

```
[1,2,3]
```

Permutations

```
123

132

213

231

312

321
```

Formula

```
n!
```

Example

```
3!

=

3×2×1

=

6
```

---

# Recursion Idea Behind Permutations

Pick one element.

Fix it.

Generate permutations of remaining elements.

Example

```
123

Fix 1

→ 23

Fix 2

→ 13

Fix 3

→12
```

---

# Difference Between Subsets and Permutations

Subsets

Order does NOT matter

Example

```
[1,2]

=

[2,1]
```

Both represent the same subset.

Total

```
2^n
```

---

Permutations

Order matters

```
123

321
```

are different.

Total

```
n!
```

---

# Time Complexity

Simple Recursion

Usually

```
O(n)
```

Factorial

```
O(n)
```

Fibonacci

```
O(2^n)
```

Subsets

```
O(2^n)
```

Permutations

```
O(n!)
```

Backtracking

Depends on problem.

Worst case is usually exponential.

---

# Common Interview Problems

Easy

✔ Factorial

✔ Power Function

✔ Fibonacci

✔ Sum of Array

✔ Reverse String

Medium

✔ Generate Subsets

✔ Permutations

✔ Combination Sum

✔ Letter Combinations

✔ Palindrome Partitioning

Hard

✔ Sudoku Solver

✔ N Queens

✔ Rat in Maze

✔ Word Search

---

# Common Mistakes

❌ Forgetting Base Case

Infinite recursion

---

❌ Not moving toward Base Case

Example

```python
fun(n)
```

instead of

```python
fun(n-1)
```

---

❌ Forgetting to undo changes in Backtracking

Always remember

```python
path.append(x)

backtrack()

path.pop()
```

---

❌ Modifying the original list without restoring it

Always undo changes.

---

# Interview Tips

✔ Always identify the Base Case first.

✔ Think of recursion as solving a smaller problem.

✔ Dry-run recursion on paper.

✔ Draw recursion trees.

✔ Learn the standard backtracking template.

✔ Practice Subsets and Permutations until comfortable.

✔ Always analyze Time and Space Complexity.

---

# Cheat Sheet

Recursion
→ Function calls itself.

Base Case
→ Stops recursion.

Recursive Case
→ Calls itself.

Call Stack
→ Stores active function calls.

Recursion Tree
→ Visual representation of recursive calls.

Backtracking
→ Try → Explore → Undo.

Subset
→ Include or Exclude each element.

Permutation
→ Arrange elements in every possible order.

Subsets Count
→ 2^n

Permutations Count
→ n!

Remember

Recursion solves the problem.

Backtracking explores **all possible solutions** while undoing choices.

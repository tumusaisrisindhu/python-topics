# Linked Lists Quick Revision

## What is a Linked List?

A collection of nodes where each node stores:

- Data
- Next node reference

Example:

1 -> 2 -> 3 -> None

---

## Reverse Linked List

Use:

- prev
- current
- next_node

Steps:

1. Save next node
2. Reverse link
3. Move pointers

Complexity:

O(n)

---

## Slow Fast Pointer

Slow moves 1 step.

Fast moves 2 steps.

Used for:

- Middle node
- Cycle detection
- Palindrome problems

Complexity:

O(n)

---

## Cycle Detection

Use Floyd's Algorithm.

If slow == fast

Cycle exists.

Otherwise:

No cycle.

Complexity:

O(n)

---

## Interview Must Know

✓ Reverse List

✓ Middle Node

✓ Detect Cycle

✓ Merge Two Sorted Lists

✓ Palindrome Linked List

✓ Remove Duplicates

✓ Intersection of Lists

---

## Memory Trick

Reverse List:
prev current next

Middle Node:
slow fast

Cycle Detection:
slow fast meet

Remember:

Linked Lists are about changing links,
not moving data.

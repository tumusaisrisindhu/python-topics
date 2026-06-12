# Arrays

## Traversal

Visit every element one by one.

Time Complexity: O(n)

---

## Prefix Sum

Used for fast range sum queries.

prefix[i] = prefix[i-1] + arr[i]

Range Sum:
prefix[r] - prefix[l-1]

Time Complexity:
Build -> O(n)
Query -> O(1)

---

## Sliding Window

Used for contiguous subarray problems.

Common Uses:

- Maximum sum subarray of size k
- Average of k elements
- Longest substring

Time Complexity: O(n)

---

## Two Pointers

Use two indices to reduce nested loops.

Common Uses:

- Pair sum
- Sorted arrays
- Palindrome check

Time Complexity: O(n)

---

## Important Interview Problems

1. Two Sum
2. Best Time To Buy Stock
3. Maximum Subarray
4. Product Of Array Except Self
5. Move Zeroes

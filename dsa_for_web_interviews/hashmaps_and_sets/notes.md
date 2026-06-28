# Day 13 - HashMaps & Sets

## What is a HashMap?

A HashMap stores data in key-value pairs.

Python:
dictionary = {}

Example:

student = {
    "name": "John",
    "age": 21
}

print(student["name"])

Output:
John

------------------------------------

## Why Use HashMaps?

Without HashMap:

Find frequency of number:

[1,2,2,3,3,3]

Need nested loops.

Time Complexity:
O(n²)

With HashMap:

frequency = {}

for num in nums:
    frequency[num] = frequency.get(num,0) + 1

Time Complexity:
O(n)

------------------------------------

## Frequency Map

Stores how many times something appears.

Example:

word = "banana"

frequency = {
    b:1,
    a:3,
    n:2
}

Used in:

- Duplicate detection
- Character counting
- Anagrams
- Voting systems

------------------------------------

## What is a Set?

Set stores only unique values.

Example:

nums = {1,2,3}

nums.add(4)

print(nums)

Output:
{1,2,3,4}

------------------------------------

## Why Use Sets?

Fast lookup.

Example:

seen = set()

for num in nums:
    if num in seen:
        print("Duplicate Found")
    seen.add(num)

Lookup:
O(1)

------------------------------------

## Caching Concept

Caching means storing results of expensive operations.

Example:

2 + 2

Instead of calculating again:

cache = {
    "2+2": 4
}

Next time return value directly.

------------------------------------

## Real World Examples

Browser Cache
Google Search Suggestions
Redis Cache
API Response Cache
User Session Storage

------------------------------------

## Interview Tip

Whenever problem asks:

- Count frequency
- Find duplicate
- Find unique
- Fast lookup

Think:

HashMap or Set
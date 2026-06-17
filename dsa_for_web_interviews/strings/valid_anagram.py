def is_anagram(s, t):
    return sorted(s) == sorted(t)


print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
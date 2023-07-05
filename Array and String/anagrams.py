# Problem 3
# Write a function that takes two strings and returns True if they are anagrams.
# For example: "heart" and "earth" are anagrams, so the function should return True.


def anagrams(s1, s2):
    if char_count(s1) == char_count(s2):
        return True
    return False


def char_count(s):
    hash_map = {}

    for c in s:
        if c not in hash_map:
            hash_map[c] = 0
        hash_map[c] += 1

    return hash_map


# some test cases
print(anagrams("heart", "earth"))  # True
print(anagrams("cats", "tocs"))  # False

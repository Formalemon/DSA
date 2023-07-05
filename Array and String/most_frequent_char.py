# Problem 4
# Write a function that takes in a string and returns the character
# that appears the most times in the string.
# For example, if the input was 'abcccccccd', the output should be 'c'
# because 'c' appears 7 times in the string,


def most_frequent_char(s):
    hash_map = {}
    max_count_char = s[0]

    for c in s:
        if c not in hash_map:
            hash_map[c] = 0
        hash_map[c] += 1

    for c in s:
        if hash_map[max_count_char] < hash_map[c]:
            max_count_char = c

    return max_count_char


# some test cases
print(most_frequent_char("abcccccccd"))  # should return 'c'
print(most_frequent_char("bookeeper"))  # should return 'e'
print(most_frequent_char("potato"))  # should return 'o'

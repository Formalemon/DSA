# Problem 1
# Write a function that takes in a compressed string and returns the uncompressed
# version of the string.
# For example, if the input is '4a3b2c1d2a', the output should be 'aaaabbbccdaa'.


def uncompress(s):
    count = ""
    new_string = ""

    for c in s:
        if not c.isalpha():
            count += c
        else:
            new_string += c * int(count)
            count = ""

    return new_string


# some test cases
print(uncompress("4a3b2c1d2a"))  # should return 'aaaabbbccdaa'
print(uncompress("2a3b4c5d6e"))  # should return 'aabbbccccddddddeeeeeee'
print(uncompress("abcd"))  # should return 'abcd'

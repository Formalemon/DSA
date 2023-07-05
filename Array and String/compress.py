# Problem 2
# Write a function that takes in a string and returns a compressed version of the string
# For example, if the input is 'aaaabbbccdaa', the output should be '4a3b2cd2a'.


def compress(s):
    current_char = s[0]
    new_string = ""
    count = 0

    for c in s:
        if c == current_char:
            count += 1
        else:
            if count == 1:
                new_string += current_char
            else:
                new_string += str(count) + current_char
            current_char = c
            count = 1

    if count == 1:
        new_string += current_char
    else:
        new_string += str(count) + current_char

    return new_string


# some test cases
print(compress("aaaabbbccdaa"))  # should return '4a3b2cd2a'
print(compress("a"))  # should return 'a'
print(compress("aa"))  # should return '2a'

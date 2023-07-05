# Problem 7
# Write a function that takes in two lists and
# returns a list of the elements that are common between the lists.
# For example, if the inputs were [1, 2, 3, 4, 5] and [3, 4, 5, 6],
# the output should be [3, 4, 5]


def intersection(a, b):
    if len(a) <= len(b):
        return find_elements(a, b)
    return find_elements(b, a)


def find_elements(a, b):
    new_list = []
    hash_set = set()

    for num in b:
        hash_set.add(num)

    for num in a:
        if num in hash_set:
            new_list.append(num)

    return new_list


# some test cases
print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6]))  # should return [3, 4, 5]
print(intersection([9, 8, 7], [7, 8, 9]))  # should return [7, 8, 9]
print(intersection([1, 2, 3], [4, 5, 6]))  # should return []

# advanced test case
a = [i for i in range(50000)]
b = [i for i in range(50000)]
print(intersection(a, b))  # should return [i for i in range(50000)]

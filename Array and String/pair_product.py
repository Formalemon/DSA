# Problem 6
# Write a function that takes in a list of numbers and a target product and
# return the indices two numbers in the list that multiply up to the target value.
# For example, if the input was ([1, 2, 3, 4, 5], 20), the output should be (3, 4)


def pair_product(numbers, target_product):
    hash_map = {}

    for i, num in enumerate(numbers):
        complement = target_product / num

        if complement in hash_map:
            return (hash_map[complement], i)

        hash_map[num] = i


# some test cases
print(pair_product([1, 2, 3, 4, 5], 20))  # should return (3, 4)
print(pair_product([6, 2, 5, 4, 1], 10))  # should return (1, 2)
print(pair_product([9, 9], 81))  # should return (0, 1)

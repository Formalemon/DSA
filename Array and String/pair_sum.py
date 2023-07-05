# Problem 5
# Write a function that takes in a list of numbers and a target sum and
# return the indices two numbers in the list that add up to the target value.
# For example, if the input was ([1, 2, 3, 4, 5], 7), the output should be (2, 3)


def pair_sum(numbers, target_sum):
    hash_map = {}

    for i, num in enumerate(numbers):
        if target_sum - num in hash_map:
            return (hash_map[target_sum - num], i)

        hash_map[num] = i


# some test cases
print(pair_sum([1, 2, 3, 4, 5], 7))  # should return (2, 3)
print(pair_sum([6, 3, 1, 4, 5], 10))  # should return (0, 3)
print(pair_sum([9, 9], 18))  # should return (0, 1)

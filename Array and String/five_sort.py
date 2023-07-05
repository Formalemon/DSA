# Problem 8
# Write a function that takes in a list of numbers
# and rearranges the numbers such that all the 5s appear at the end of the list.
# For example, if the input was [1, 5, 3, 5, 5, 2, 4]
# the output should be [1, 4, 3, 2, 5, 5, 5]


def five_sort(nums):
    i, j = 0, len(nums) - 1

    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            i += 1

    return nums


# some test cases
print(five_sort([1, 5, 3, 5, 5, 2, 4]))  # should return [1, 4, 3, 2, 5, 5, 5]
print(
    five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
)  # should return [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]

# advanced test case
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
print(five_sort(nums))  # should return [4, 4, 4, ..., 5, 5, 5]

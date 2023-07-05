# Problem 1
# Write a function that takes the head node of a linked list and
# returns the sum of all nodes in the list.
# Example: 1 -> 2 -> 3 -> 4 -> 5 -> None should return 15


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


# recursive
def sum_list_r(head):
    if head is None:
        return 0
    return head.data + sum_list_r(head.next)


# iterative
def sum_list_i(head):
    total_sum = 0
    current = head
    while current:
        total_sum += current.data
        current = current.next

    return total_sum


# Test
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(sum_list_r(a))  # 10
print(sum_list_i(a))  # 10

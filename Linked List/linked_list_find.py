# Problem 2
# Write a function that takes the head node of a linked list and a target value
# and returns True if the target is in the list and False otherwise.
# Example: 1 -> 2 -> 3 -> 4 -> 5 -> None should return True if the target is 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


def linked_list_find(head, target):
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next

    return False


# Test
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(linked_list_find(a, 3))  # True
print(linked_list_find(a, 5))  # False

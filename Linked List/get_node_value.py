# Problem 3
# Write a function that takes the head node of a linked list and an index and
# returns the value of the node at that index position.
# Example: 1 -> 2 -> 3 -> 4 -> 5 -> None should return 3 if the index is 2


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


def get_node_value(head, index):
    current = head
    current_index = 0
    while current:
        if current_index == index:
            return current.data
        current = current.next
        current_index += 1

    return None


# Test
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(get_node_value(a, 2))  # 3
print(get_node_value(a, 5))  # None

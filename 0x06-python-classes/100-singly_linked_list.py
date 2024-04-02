#!/usr/bin/python3
class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList with an empty head."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

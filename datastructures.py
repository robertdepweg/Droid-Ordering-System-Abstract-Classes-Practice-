"""Data structure code"""

# Robert Depweg
# CIS 226
# 10-25-2024


class Stack:
    """Last in, first out with linked list"""

    class Node:
        """Node in a data structure"""

        def __init__(self):
            """Constructor"""
            self.data = None
            self.next = None

    def __init__(self):
        """Constructor"""
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, data):
        """Add a new element to the back of the linked list."""
        # Pointer to old tail is created
        old_tail = self._tail
        # New node assigned to tail
        self._tail = self.Node()
        # Assigns data while assigning next pointed
        self._tail.data = data
        # Increment the size of the list
        self._size += 1
        # Check to see if the list was empty. If so, make the head point
        # to the same location as the tail
        if self._size == 1:
            self._head = self._tail
        else:
            old_tail.next = self._tail

    def pop(self):
        """Remove an element from the front of the linked list"""
        if self._head is None:
            return
        # Let's get the data to return
        data = self._head.data
        # Move the head pointer to the next in the list
        self._head = self._head.next
        # Decrease the size of the list.
        self._size -= 1

        # Check to see if we just removed the last node from the list.
        if self._head is None:
            # If so, tail needs to be set to None
            self._tail = None

        # Return the data from the removed node
        return data


class Queue:
    """First in, first out using linked list"""

    class Node:
        """Node in a data structure"""

        def __init__(self):
            """Constructor"""
            self.data = None
            self.next = None

    def __init__(self):
        """Constructor"""
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data):
        """Add a new element to front of the linked list."""
        # Make a new variable to also reference the head of the list.
        # It be released at the end by the garbage collector when out
        # of scope of function.
        old_head = self._head
        # Make a new node and assign it to the head variable
        self._head = self.Node()
        # Set the data on the new Node
        self._head.data = data
        # Make the next pointer property of the Node point to the old head.
        self._head.next = old_head
        # Increment the size of the list
        self._size += 1
        # Ensure that if we are adding the very first node to the linked list,
        # the tail will be pointing to the new node we create.
        # Otherwise, do nothing.
        if self._size == 1:
            self._tail = self._head

    def dequeue(self):
        """Remove an element from front of linked list"""
        # Let's get the data to return
        data = self._head.data
        # Move the head pointer to the next in the list
        self._head = self._head.next
        # Decrease the size of the list.
        self._size -= 1

        # Check to see if we just removed the last node from the list.
        if self._head is None:
            # If so, tail needs to be set to None
            self._tail = None

        # Return the data from the removed node
        return data

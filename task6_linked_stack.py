from node import Node


class LinkedStackADT:
    def __init__(self):
        """
        This method initialises the instance attribute top to point to None
        :return: none
        :raises: no exceptions
        :pre-condition: none
        :post-condition: none
        :complexity: O(1) constant time
        """
        self.top = None

    def is_empty(self):
        """
        This method determines if the stack is empty, by checking if self.top points to None
        :return: true if stack is empty, false otherwise.
        :raises: no exceptions
        :pre-condition: none
        :post-condition: returns boolean type
        :complexity: O(1) constant time
        """
        return self.top is None

    def push(self, item):
        """
        This method pushes an item onto the top of the stack
        :return: none
        :raises: no exceptions
        :pre-condition: none
        :post-condition: size of stack increased by 1
        :complexity: O(1) constant time
        """
        self.top = Node(item, self.top)

    def pop(self):
        """
        This method pops the item at the top of the stack
        :return: item at the top of stack
        :raises: StopIteration if the stack is empty
        :pre-condition: none
        :post-condition: returns the item at the top of the stack, size of the stack decreased by 1
        :complexity: O(1) constant time
        """
        if self.is_empty():
            raise StopIteration("The stack is empty!!")
        item = self.top.item
        self.top = self.top.next
        return item

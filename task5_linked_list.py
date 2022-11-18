from node import Node


class LinkedListADT:
    def __init__(self):
        """
        This method initialises instance attributes with start as None, and count as 0
        :return: none
        :raises: no exceptions
        :pre-condition: none
        :post-condition: none
        :complexity: O(1) constant time
        """
        self.start = None
        self.count = 0

    def __len__(self):
        """
        This method finds the length of the list
        :return: length of the list
        :raises: no exceptions
        :pre-condition: none
        :post-condition: length of list is integer type
        :complexity: O(1) constant time
        """
        return self.count

    def __str__(self):
        """
        This method puts every element of the list into a string with a newline at the end of element
        :param: none
        :return: string of the list
        :raises: no exceptions
        :pre-condition: none
        :post-condition: return value is a string type of the list
        :complexity: O(n), depending on size of the list
        """
        out_string = ""
        current_node = self.start
        while current_node is not None:
            out_string += "{}\n".format(str(current_node))
            current_node = current_node.next
        return out_string

    def __getitem__(self, index):
        """
        This method returns the value at the given index of the list
        :param: index(int) of the list
        :return: element at given index
        :raises: ValueError if index is not an integer; IndexError if given index not in range
        :pre-condition: -len(self) <= index <= len(self)
        :post-condition: returns item at given index
        :complexity: O(1), constant time
        """
        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.index_valid(index):
            raise IndexError("index is out of range")

        if index >= 0:
            node = self._get_node(index)
            return node.item

        else:
            other_node = self._get_node(len(self) + index)
            return other_node.item

    def is_empty(self):
        """
        This method determines if the list is empty or not
        :return: true if list is empty, false otherwise
        :raises: no exceptions
        :pre-condition: none
        :post-condition: returns boolean type
        :complexity: O(1) constant time
        """
        return self.start is None

    def index_valid(self, index):
        """
        This method determines if the given index is within the range of the list
        :return: true if index is within the range of the list, false otherwise.
        :raises: no exceptions
        :pre-condition: none
        :post-condition: returns boolean type
        :complexity: O(1) constant time
        """
        return -len(self) <= index <= len(self)

    def _get_node(self, index):
        """
        This method returns the node at the given index
        :return: node at index
        :raises: ValueError if index is not an integer type, IndexError if given index is out of range
        :pre-condition: index is integer type and within the range of the list
        :post-condition: node object at index of the list
        :complexity: O(n), depending on size of the list
        """
        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.index_valid(index):
            raise IndexError("index is out of range")
        my_node = self.start

        if index >= 0:
            for _ in range(index):
                my_node = my_node.next

        else:
            for _ in range(len(self) + index):
                my_node = my_node.next

        return my_node

    def insert(self, index, item):
        """
        This method inserts an item at a given index into the list
        :param: index(int) of the list and item
        :return: none
        :raises: ValueError if index is not an integer, IndexError if index not in range
        :pre-condition: -len(self) <= index <= len(self), index is integer type, list is not full
        :post-condition: current size += 1
        :complexity: O(1), constant time
        """
        if not self.index_valid(index):
            raise IndexError("index is out of range")

        if index == 0:
            self.start = Node(item, self.start)

        else:
            if index > 0:
                fresh_node = self._get_node(index - 1)
                fresh_node.next = Node(item, fresh_node.next)

            else:
                new_node = self._get_node(len(self) + index - 1)
                new_node.next = Node(item, new_node.next)

        self.count += 1

    def delete(self, index):
        """
        This method deletes the element at the given index in the list
        :param: index(int) in the list
        :return: none
        :raises: StopIteration if list is empty, ValueError if index is not an integer,
                 IndexError if given index out of range
        :pre-condition: -len(self) <= index <= len(self), index is integer type
        :post-condition: current size -= 1
        :complexity: O(1), constant time
        """
        if self.is_empty():
            raise StopIteration("the list is empty")

        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.index_valid(index):
            raise IndexError("index is out of range")

        if index == 0:
            self.start = self.start.next

        else:
            if index > 0:
                a_node = self._get_node(index - 1)
                a_node.next = a_node.next.next
            else:
                this_node = self._get_node(len(self) + index - 1)
                this_node.next = this_node.next.next

        self.count -= 1

    def append(self, item):
        """
        This method appends an item into the list
        :param: item
        :return: none
        :raises: no exceptions
        :pre-condition: list is not full
        :post-condition: current size += 1
        :complexity: O(1), constant time
        """
        if len(self) == 0:
            self.start = Node(item, self.start)
        else:
            tail_node = self._get_node(len(self) - 1)
            tail_node.next = Node(item)

        self.count += 1

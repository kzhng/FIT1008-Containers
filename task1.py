from referential_array import build_array


class ListADT:
    def __init__(self):
        """
        This method initialises an array of size 50, max size of list and current size of list attributes
        :return: none
        :raises: no exceptions
        :pre-condition: none
        :post-condition: none
        :complexity: O(1) constant time
        """
        self._array = build_array(50)
        self.maxSize = 50
        self.currentSize = 0

    def __str__(self):
        """
        This method puts every element of the list into a string with a newline at the end of element
        :param: none
        :return: string of the list
        :raises: no exceptions
        :pre-condition: none
        :post-condition: return value is a string type of the list
        :complexity: O(1), fixed array length
        """
        output_string = ""
        for i in range(len(self)):
            output_string += "{}\n".format(self._array[i])
        return output_string

    def __len__(self):
        """
        This method returns the length of the list
        :param: none
        :return: length of the list
        :raises: no exceptions
        :pre-condition: none
        :post-condition: return integer value
        :complexity: O(1), constant time
        """
        return self.currentSize

    def __contains__(self, item):
        """
        This method determines if an element is in the list or not
        :param: item(int) of the list
        :return: true if the item is in the list, false otherwise.
        :raises: no exceptions
        :pre-condition: none
        :post-condition: returns boolean type
        :complexity: O(1), fixed array length
        """
        for j in range(len(self)):
            if item == self._array[j]:
                return True
        return False

    def __getitem__(self, index):
        """
        This method returns the value at the given index of the list
        :param: index(int) of the list
        :return: element at given index
        :raises: ValueError if index is not an integer; IndexError if given index not in range
        :pre-condition: none
        :post-condition: returns item at given index
        :complexity: O(1), constant time
        """
        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.valid_index(index):
            raise IndexError("index not in range")

        if index >= 0:
            return self._array[index]
        if index < 0:
            return self._array[len(self) + index]

    def __setitem__(self, index, item):
        """
        This method sets a given index to be a given item in the list
        :param: index(int) of the list and item
        :return: none
        :raises: ValueError if index is not an integer; IndexError if given index not in range
        :pre-condition: -len(self) <= index <= len(self), index is integer type
        :post-condition: none
        :complexity: O(1), constant time
        """
        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.valid_index(index):
            raise IndexError("index not in range")

        if index >= 0:
            self._array[index] = item
        if index < 0:
            self._array[len(self) + index] = item

    def __eq__(self, other):
        """
        This method determines if the instance list is equal to another list
        :param: a list(list)
        :return: true if the list is the same, false otherwise.
        :raises: ValueError if other is not a list
        :pre-condition: none
        :post-condition: return value is boolean
        :complexity: O(1), constant time
        """
        if not isinstance(other, list):
            raise ValueError("must compare list with list")

        return self._array == other

    def append(self, item):
        """
        This method appends an item into the list
        :param: item
        :return: none
        :raises: StopIteration if list is full
        :pre-condition: list is not full
        :post-condition: current size += 1
        :complexity: O(1), constant time
        """
        if self.is_full():
            raise StopIteration("the array is full")

        self._array[len(self)] = item
        self.currentSize += 1

    def insert(self, index, item):
        """
        This method inserts an item at a given index into the list
        :param: index(int) of the list and item
        :return: none
        :raises: StopIteration if list is full, ValueError if index is not an integer, IndexError if index not in range
        :pre-condition: -len(self) <= index <= len(self), index is integer type, list is not full
        :post-condition: current size += 1
        :complexity: O(1), fixed array length
        """
        if self.is_full():
            raise StopIteration("the array is full")

        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.valid_index(index):
            raise IndexError("index not in range")

        pointer = len(self)
        if index >= 0:
            while pointer > index:
                self._array[pointer] = self._array[pointer - 1]
                pointer -= 1
            self._array[index] = item

        if index < 0:
            while pointer > len(self) + index:
                self._array[pointer] = self._array[pointer - 1]
                pointer -= 1
            self._array[len(self) + index] = item
        self.currentSize += 1

    def remove(self, item):
        """
        This method removes the first instance of the given item in the list
        :param: item
        :return: none
        :raises: ValueError when given item is not in the list
        :pre-condition: item in list
        :post-condition: current size -= 1
        :complexity: O(1), fixed array length
        """
        if item not in self._array:
            raise ValueError("item not in list")

        removed = False
        k = 0
        while not removed and k < len(self):
            if self._array[k] == item:
                pointer = k
                while pointer < len(self):
                    self._array[pointer] = self._array[pointer + 1]
                    pointer += 1
                removed = True
            k += 1
        self.currentSize -= 1

    def delete(self, index):
        """
        This method deletes the element at the given index in the list
        :param: index(int) in the list
        :return: none
        :raises: StopIteration if list is empty, ValueError if index is not an integer,
                 IndexError if given index out of range
        :pre-condition: -len(self) <= index <= len(self), index is integer type
        :post-condition: current size -= 1
        :complexity: O(1), fixed array length
        """
        if self.is_empty():
            raise StopIteration("the list is empty")

        if not isinstance(index, int):
            raise ValueError("index must be an integer")

        if not self.valid_index(index):
            raise IndexError("index not in range")

        if index >= 0:
            pointer = index
            while pointer < len(self):
                self._array[pointer] = self._array[pointer + 1]
                pointer += 1

        if index < 0:
            pointer_neg = len(self) + index
            while pointer_neg < len(self):
                self._array[pointer_neg] = self._array[pointer_neg + 1]
                pointer_neg += 1
        self.currentSize -= 1

    def swap(self, pos1, pos2):
        """
        This method swaps the elements at pos1 and pos2 in the list with each other
        :param: 2 positions(int) in the list
        :return: none
        :raises: no exceptions
        :pre-condition: pos1, pos2 are integer type and within index range of the list
        :post-condition: elements at pos1 and pos2 are swapped
        :complexity: O(1), constant time
        """
        temp = self._array[pos1]
        self._array[pos1] = self._array[pos2]
        self._array[pos2] = temp

    def valid_index(self, index):
        """
        This method determines if a given index of the list is out of range or not
        :param: index(int) in the list
        :return: True if index is in range -len(self) to len(self), false otherwise.
        :raises: no exceptions
        :pre-condition: index is integer type
        :post-condition: returns boolean type
        :complexity: O(1), constant time
        """
        return -len(self) <= index <= len(self)

    def is_empty(self):
        """
        This method determines if the list if empty or not
        :param: none
        :return: true if the list is empty, false otherwise.
        :raises: no exceptions
        :pre-condition: none
        :post-condition: return boolean type
        :complexity: O(1) constant time
        """
        return self.currentSize == 0

    def is_full(self):
        """
        This method determines if the list if full or not
        :param: none
        :return: true if the list is full, false otherwise.
        :raises: no exceptions
        :pre-condition: none
        :post-condition: return boolean type
        :complexity: O(1) constant time
        """
        return len(self) >= self.maxSize

    def sort(self, reverse=False):
        """
        This method sorts the list in ascending or descending order depending on user input
        :param: reverse sort(bool)
        :return: none
        :raises: no exceptions
        :pre-condition: reverse is boolean type if a parameter is given
        :post-condition: list is sorted in ascending order or descending order depending on reverse
        :complexity: O(1), fixed array length
        """
        if not isinstance(reverse, bool):
            raise ValueError("reverse must be boolean")

        if reverse:
            for c in range(1, len(self)):
                d = c
                while d > 0 and self._array[d] > self._array[d - 1]:
                    self.swap(d, d-1)
                    d -= 1
        if not reverse:
            for e in range(1, len(self)):
                f = e
                while f > 0 and self._array[f] < self._array[f - 1]:
                    self.swap(f, f-1)
                    f -= 1

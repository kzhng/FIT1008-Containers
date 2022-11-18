from task5_linked_list import LinkedListADT
from task3 import file_to_list


class TextEditor:
    def __init__(self):
        """
        This method declares an instance attribute to be a list type
        :return: none
        :raises: no exceptions
        :pre-condition: none
        :post-condition: none
        :complexity: O(1) constant time
        """
        self._my_list = LinkedListADT()

    def insert_num(self, num, text):
        """
        This method inserts a line of text into the list at index num
        :return: none
        :raises: no exceptions
        :pre-condition: num is within the index range of the list
        :post-condition: size of list += 1
        :complexity: O(1) constant time
        """
        self._my_list.insert(num, text)

    def read_filename(self, filename):
        """
        This method reads a filename and appends every line of the file onto the list
        :return: none
        :raises: no exceptions
        :pre-condition: filename is of python or text type
        :post-condition: size of list += number of lines in file
        :complexity: O(n), depending on number of lines in file
        """
        file_list = file_to_list(filename)
        for i in range(len(file_list)):
            self._my_list.append(file_list[i])

    def write_filename(self, file_name):
        """
        This method writes every element of the list into a file
        :return: none
        :raises: no exceptions
        :pre-condition: filename is of python or text type. if filename does not exist,
                        it will create one with the filename
        :post-condition: a file with every element of the list in a separate line in order
        :complexity: O(n), depending on length of list
        """
        file = open(file_name, 'a')
        file.write(str(self._my_list))
        file.close()

    def print_lines(self, num1, num2):
        """
        This method returns a string containing every line from num1 to num2 in the list
        :return: string with every line from num1 to num2
        :raises: no exceptions
        :pre-condition: none
        :post-condition: string type
        :complexity: O(n), depending on how big the range is
        """
        out_string = ""
        for i in range(num1, num2):
            out_string += "{}\n".format(self._my_list[i])
        return out_string

    def delete_num(self, num="all"):
        """
        This method deletes the element at the given index num in the list. if no parameter is given, delete entire list
        :return: none
        :raises: no exceptions
        :pre-condition: num is of integer type if a parameter is given
        :post-condition: size of list -= 1 if parameter for num is given
                         size of list = 0 if no parameter for num is given
        :complexity: O(1), constant time
        """
        if num != "all":
            self._my_list.delete(num)
        else:
            self._my_list.__init__()

    def search_word(self, word):
        """
        This method finds the line number in which word appears
        :return: a string containing the line numbers in which word appears in the list
        :raises: no exceptions
        :pre-condition: none
        :post-condition: string type
        :complexity: O(n), depending on size of list
        """
        line_number_string = ""
        for i in range(len(self._my_list)):
            text = self._my_list[i]
            text = text.lower()
            if word in text:
                line_number_string += "{}, ".format(i)
        return line_number_string

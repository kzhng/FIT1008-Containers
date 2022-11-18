from task2 import ListADT


def file_to_list(file_name):
    if not isinstance(file_name, str):
        raise ValueError("file name must be a string")

    if (file_name[-3:] != ".py") and (file_name[-4:] != ".txt"):
        raise ValueError("file name must be python or text type")
    """
    This function puts every line in the given file into a list
    :return: a list containing every line in the file
    :raises: ValueError if the filename is not a string, text or python type
    :pre-condition: none
    :post-condition: none
    :complexity: O(n), depending on how many lines the file has
    """
    file = open(file_name, 'r')
    file_list = ListADT()
    for line in file:
        line_string = line.strip()
        line_string = line_string
        file_list.append(line_string)
    file.close()
    return file_list

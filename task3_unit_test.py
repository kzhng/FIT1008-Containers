from task3 import file_to_list


def test_file_to_list():
    try:
        file_to_list(13)
        assert False, "Test Failed: ValueError not triggered when an integer is given as a filename"
    except ValueError:
        assert True

    try:
        file_to_list(5.24)
        assert False, "Test Failed: ValueError not triggered when a float is given as a filename"
    except ValueError:
        assert True

    try:
        file_to_list("hello_world")
        assert False, "Test Failed: ValueError not triggered for incorrect file type"
    except ValueError:
        assert True

    err_list = file_to_list("blah.py")
    b_list_string = "ehdfh\ndfghfd\ngfdg\ndfgdfgfd\n"
    assert str(err_list) == b_list_string, "Test failed: file to list not correct conversion"
    err_list_two = file_to_list("blah2.py")
    assert str(err_list_two) == "", "Test Failed: empty file into string != empty string"


if __name__ == '__main__':
    test_file_to_list()
    print("All tests passing...")

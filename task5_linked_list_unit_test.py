from task5_linked_list import LinkedListADT


def test_len():
    a_list = LinkedListADT()
    assert len(a_list) == 0, "Test failed: length of [] != 0"
    b_list = LinkedListADT()
    b_list.append(10)
    b_list.append(34)
    b_list.append(6)
    assert len(b_list) == 3, "Test failed: length of [10,34,6] != 3"


def test_str():
    a_list = LinkedListADT()
    a_list.append(4)
    assert str(a_list) == "4\n", "Test failed: 10 != 10"
    b_list = LinkedListADT()
    b_list.append(10)
    b_list.append(34)
    b_list.append(6)
    assert str(b_list) == "10\n34\n6\n", "Test failed: 10\n34\n6\n != 10\n34\n6\n"


def test_getitem():
    try:
        err_list = LinkedListADT()
        err_list["s"]
        assert False, "Test failed: getitem ValueError not triggered for string"
    except ValueError:
        assert True

    try:
        err_list = LinkedListADT()
        err_list[1.22]
        assert False, "Test failed: getitem ValueError not triggered for float"
    except ValueError:
        assert True

    try:
        err_list = LinkedListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[7]
        assert False, "Test failed: getitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    try:
        err_list = LinkedListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-7]
        assert False, "Test failed: getitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    a_list = LinkedListADT()
    a_list.append(3)
    a_list.append(4)
    a_list.append(7)
    assert a_list[2] == 7, "Test failed: index 2 of [3,4,7] != 4"
    assert a_list[-3] == 3, "Test failed: index -3 of [3,4,7] != 3"


def test_is_empty():
    a_list = LinkedListADT()
    assert a_list.is_empty(), "Test failed: empty list true != true"
    b_list = LinkedListADT()
    b_list.append(4)
    b_list.append(5)
    b_list.append(6)
    assert not b_list.is_empty(), "Test failed: list empty false != false"


def test_index_valid():
    a_list = LinkedListADT()
    a_list.append(2)
    a_list.append(3)
    a_list.append(4)
    assert a_list.index_valid(1), "Test failed: [2,3,4] 1 valid index true != true"
    assert a_list.index_valid(-2), "Test failed: [2,3,4] -2 valid index true != true"
    assert not a_list.index_valid(4), "Test failed: [2,3,4] 3 valid index false != true"
    assert not a_list.index_valid(-4), "Test failed: [2,3,4] -4 valid index false != false"


def test_insert():
    try:
        err_list = LinkedListADT()
        err_list["y"]
        assert False, "Test failed: insert ValueError not triggered for string"
    except ValueError:
        assert True
    try:
        err_list = LinkedListADT()
        err_list[45.56]
        assert False, "Test failed: insert ValueError not triggered for float"
    except ValueError:
        assert True
    try:
        err_list = LinkedListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[7]
        assert False, "Test failed: insert IndexError not triggered for index out of range"
    except IndexError:
        assert True
    try:
        err_list = LinkedListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-5]
        assert False, "Test failed: insert IndexError not triggered for index out of range"
    except IndexError:
        assert True

    err_list = LinkedListADT()
    for i in range(50):
        err_list.insert(i, i)
    b_list_string = ""
    for j in range(50):
        b_list_string += "{}\n".format(j)
    assert str(err_list) == b_list_string, "Test failed: list of 1 to 50 != list of 1 to 50"
    err_list_two = LinkedListADT()
    for k in range(90):
        err_list.insert(k, k)
    c_list_string = ""
    for m in range(90):
        b_list_string += "{}\n".format(m)
    assert str(err_list_two) == c_list_string, "Test failed: list of 1 to 90 != list of 1 to 90"


def test_delete():
    try:
        err_list = LinkedListADT()
        err_list.delete(0)
        assert False, "Test Failed: deleting something from empty list is not possible"
    except StopIteration:
        assert True

    try:
        err_list = LinkedListADT()
        err_list["p"]
        assert False, "Test failed: delete ValueError not triggered for string"
    except ValueError:
        assert True

    try:
        err_list = LinkedListADT()
        err_list[0.00]
        assert False, "Test failed: delete ValueError not triggered for float"
    except ValueError:
        assert True

    try:
        err_list = LinkedListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[8]
        assert False, "Test failed: delete IndexError not triggered for index out of range"
    except IndexError:
        assert True

    err_list = LinkedListADT()
    for i in range(50):
        err_list.append(10)
    for j in range(44):
        err_list.delete(0)
    b_list_string = ""
    for k in range(6):
        b_list_string += "{}\n".format(10)
    assert str(err_list) == b_list_string, "Test failed: delete 44 10's at index 0 from a list of 50 10's" \
                                           "!= a list of 6 10's"
    err_list_two = LinkedListADT()
    for m in range(18):
        err_list_two.append(7)
    for n in range(16):
        err_list_two.delete(0)
    c_list_string = ""
    for p in range(2):
        c_list_string += "{}\n".format(7)
    assert str(err_list_two) == c_list_string, "Test failed: removing 16 7's at index 0 from a list of 18 7's" \
                                               "!= a list of 2 7's"
    err_list_three = LinkedListADT()
    err_list_three.append(3)
    err_list_three.delete(0)
    assert str(err_list_three) == "", "Test failed: deleting at index 0 for list 3 != empty list"


def test_append():
    err_list = LinkedListADT()
    for i in range(50):
        err_list.append(i)
    b_list_string = ""
    for j in range(50):
        b_list_string += "{}\n".format(j)
    assert str(err_list) == b_list_string, "Test failed: list of 1 to 50 != list of 1 to 50"
    err_list_two = LinkedListADT()
    for k in range(90):
        err_list.append(k)
    c_list_string = ""
    for m in range(90):
        b_list_string += "{}\n".format(m)
    assert str(err_list_two) == c_list_string, "Test failed: list of 1 to 90 != list of 1 to 90"


if __name__ == '__main__':
    test_len()
    test_str()
    test_getitem()
    test_is_empty()
    test_index_valid()
    test_insert()
    test_delete()
    test_append()
    print("All tests passing...")

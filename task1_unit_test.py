from task1 import ListADT


def test_append():
    try:
        err_list = ListADT()
        for foo in range(50):
            err_list.append(foo)
        err_list.append(23)
        assert False, "Test failed: StopIteration for append not triggered when list is full"
    except StopIteration:
        assert True

    a_list = ListADT()
    a_list.append(10)
    assert a_list[0] == 10, "Test failed: [10] != [10]"
    b_list = ListADT()
    b_list.append(10)
    b_list.append(12)
    assert b_list[1] == 12, "Test failed: 12 != 12"


def test_str():
    a_list = ListADT()
    a_list.append(4)
    assert str(a_list) == "4\n", "Test failed: 10 != 10"
    b_list = ListADT()
    b_list.append(10)
    b_list.append(34)
    b_list.append(6)
    assert str(b_list) == "10\n34\n6\n", "Test failed: 10\n34\n6\n != 10\n34\n6\n"


def test_len():
    a_list = ListADT()
    assert len(a_list) == 0, "Test failed: length of [] != 0"
    b_list = ListADT()
    b_list.append(10)
    b_list.append(34)
    b_list.append(6)
    assert len(b_list) == 3, "Test failed: length of [10,34,6] != 3"


def test_contains():
    a_list = ListADT()
    a_list.append(3)
    a_list.append(4)
    a_list.append(7)
    assert (4 in a_list), "Test failed: 4 in list true != true "
    assert not (5 in a_list), "Test failed: 5 not in list false != false"


def test_getitem():
    try:
        err_list = ListADT()
        err_list["s"]
        assert False, "Test failed: getitem ValueError not triggered for string"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list[1.22]
        assert False, "Test failed: getitem ValueError not triggered for float"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[7]
        assert False, "Test failed: getitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-7]
        assert False, "Test failed: getitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    a_list = ListADT()
    a_list.append(3)
    a_list.append(4)
    a_list.append(7)
    assert a_list[2] == 7, "Test failed: index 2 of [3,4,7] != 4"
    assert a_list[-3] == 3, "Test failed: index -3 of [3,4,7] != 3"


def test_setitem():
    try:
        err_list = ListADT()
        err_list["s"]
        assert False, "Test failed: setitem ValueError not triggered for string"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list[6.00]
        assert False, "Test failed: setitem ValueError not triggered for float"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[4]
        assert False, "Test failed: setitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-5]
        assert False, "Test failed: setitem IndexError not triggered for index out of range"
    except IndexError:
        assert True

    a_list = ListADT()
    a_list.append(3)
    a_list.append(4)
    a_list.append(7)
    a_list[1] = 6
    a_list[-1] = 5
    assert a_list[1] == 6, "Test failed: [3,4,7], set index 1 element to 6 != 6"
    assert a_list[-1] == 5, "Test failed: [3,6,7], set index -1 element to 5 != 5"


def test_eq():
    try:
        err_list = ListADT()
        test_list = "foobar"
        err_list == test_list
        assert False, "Test failed: eq ValueError not triggered for non list type"
    except ValueError:
        assert True
    try:
        err_list = ListADT()
        test_list = 567
        err_list == test_list
        assert False, "Test failed: eq ValueError not triggered for non list type"
    except ValueError:
        assert True

    a_list = ListADT()
    a_list.append(3)
    a_list.append(4)
    a_list.append(7)
    b_list_string = "3\n4\n7\n"
    assert (str(a_list) == b_list_string), "Test failed: [3,4,7] == [3,4,7], True != True"
    c_list = ListADT()
    assert not (str(c_list) == "3\n4\n"), "Test failed: [] == [3,4], False != False"


def test_insert():
    try:
        err_list = ListADT()
        for foo in range(50):
            err_list.insert(0, foo)
        err_list.insert(23, 46)
        assert False, "Test failed: insert StopIteration not triggered when list is full"
    except StopIteration:
        assert True
    try:
        err_list = ListADT()
        err_list["y"]
        assert False, "Test failed: insert ValueError not triggered for string"
    except ValueError:
        assert True
    try:
        err_list = ListADT()
        err_list[45.56]
        assert False, "Test failed: insert ValueError not triggered for float"
    except ValueError:
        assert True
    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[7]
        assert False, "Test failed: insert IndexError not triggered for index out of range"
    except IndexError:
        assert True
    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-5]
        assert False, "Test failed: insert IndexError not triggered for index out of range"
    except IndexError:
        assert True

    a_list = ListADT()
    a_list.insert(0, 3)
    a_list.insert(0, 5)
    a_list.insert(0, 7)
    a_list.insert(1, 4)
    b_list_string = "7\n4\n5\n3\n"
    assert str(a_list) == b_list_string, "Test failed: [3,5,7] insert 4 in index 1 != [3,4,5,7]"
    c_list = ListADT()
    c_list.insert(0, 3)
    c_list.insert(0, 5)
    c_list.insert(0, 7)
    c_list.insert(-2, 4)
    d_list_string = "7\n4\n5\n3\n"
    assert str(c_list) == d_list_string, "Test failed: [3,5,7] insert 4 in index -2 != [3,4,5,7]"


def test_remove():
    try:
        err_list = ListADT()
        err_list.remove(3)
        assert False, "Test failed: remove ValueError not triggered when removing an element not contained"
    except ValueError:
        assert True
    try:
        err_list = ListADT()
        err_list.append(4)
        err_list.append(5)
        err_list.append(7)
        err_list.remove(3)
        assert False, "Test failed: remove ValueError not triggered when removing an element not contained"
    except ValueError:
        assert True

    a_list = ListADT()
    a_list.append(3)
    a_list.append(5)
    a_list.append(7)
    a_list.remove(5)
    b_list_string = "3\n7\n"
    assert str(a_list) == b_list_string, "Test failed: [3,5,7] remove 5 != [3,7]"
    c_list = ListADT()
    for foo in range(8):
        c_list.append(5)
    for bar in range(7):
        c_list.remove(5)
    d_list_string = "5\n"
    assert str(c_list) == d_list_string, "Test failed: remove all except 1 five doesnt output only 1 5"
    e_list = ListADT()
    e_list.append(6)
    e_list.append(5)
    e_list.append(5)
    e_list.append(64)
    e_list.append(5)
    e_list.append(6)
    e_list.append(5)
    e_list.append(34)
    for baz in range(4):
        e_list.remove(5)
    f_list_string = "6\n64\n6\n34\n"
    assert str(e_list) == f_list_string, "Test failed: remove elements, order of list/number of elements not maintained"


def test_delete():
    try:
        err_list = ListADT()
        err_list.delete(0)
        assert False, "Test Failed: deleting something from empty list is not possible"
    except StopIteration:
        assert True

    try:
        err_list = ListADT()
        err_list["p"]
        assert False, "Test failed: delete ValueError not triggered for string"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list[0.00]
        assert False, "Test failed: delete ValueError not triggered for float"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[8]
        assert False, "Test failed: delete IndexError not triggered for index out of range"
    except IndexError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(4)
        err_list.append(7)
        err_list[-10]
        assert False, "Test failed: delete IndexError not triggered for index out of range"
    except IndexError:
        assert True

    a_list = ListADT()
    a_list.append(3)
    a_list.append(5)
    a_list.append(7)
    a_list.delete(1)
    b_list_string = "3\n7\n"
    assert str(a_list) == b_list_string, "Test failed: [3,5,7] delete at index 1 != [3,7]"
    c_list = ListADT()
    c_list.append(3)
    c_list.append(5)
    c_list.append(7)
    c_list.delete(-2)
    d_list_string = "3\n7\n"
    assert str(c_list) == d_list_string, "Test failed: [3,5,7] delete at index -2 != [3,7]"
    e_list = ListADT()
    e_list.append(3)
    e_list.delete(0)
    assert str(e_list) == "", "Test failed: deleting at index 0 for list 3 != empty list"


def test_swap():
    a_list = ListADT()
    a_list.append(2)
    a_list.append(3)
    a_list.swap(0, 1)
    b_list_string = "3\n2\n"
    assert str(a_list) == b_list_string, "Test failed: [2,3] swap != [3,2]"


def test_valid_index():
    a_list = ListADT()
    a_list.append(2)
    a_list.append(3)
    a_list.append(4)
    assert a_list.valid_index(1), "Test failed: [2,3,4] 1 valid index true != true"
    assert a_list.valid_index(-2), "Test failed: [2,3,4] -2 valid index true != true"
    assert not a_list.valid_index(4), "Test failed: [2,3,4] 3 valid index false != true"
    assert not a_list.valid_index(-4), "Test failed: [2,3,4] -4 valid index false != false"


def test_is_empty():
    a_list = ListADT()
    assert a_list.is_empty(), "Test failed: empty list true != true"
    b_list = ListADT()
    b_list.append(4)
    b_list.append(5)
    b_list.append(6)
    assert not b_list.is_empty(), "Test failed: list empty false != false"


def test_is_full():
    a_list = ListADT()
    for foo in range(50):
        a_list.append(foo)
    assert a_list.is_full(), "Test failed: list full true != true"
    b_list = ListADT()
    assert not b_list.is_full(), "Test failed: list empty false != false"


def test_sort():
    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(5)
        err_list.append(7)
        err_list.append(1)
        err_list.sort(13)
        assert False, "Test failed: sort ValueError not triggered when integer is passed for reverse"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(5)
        err_list.append(7)
        err_list.append(1)
        err_list.sort("s")
        assert False, "Test failed: sort ValueError not triggered when string is passed for reverse"
    except ValueError:
        assert True

    try:
        err_list = ListADT()
        err_list.append(3)
        err_list.append(5)
        err_list.append(7)
        err_list.append(1)
        err_list.sort([5, 6])
        assert False, "Test failed: sort ValueError not triggered when list is passed for reverse"
    except ValueError:
        assert True

    a_list = ListADT()
    a_list.append(8)
    a_list.append(13)
    a_list.append(21)
    a_list.append(30)
    a_list.append(16)
    a_list.append(17)
    a_list.append(1)
    a_list.append(15)
    a_list.append(7)
    a_list.append(16)
    b_list_string = "1\n7\n8\n13\n15\n16\n16\n17\n21\n30\n"
    a_list.sort()
    assert str(a_list) == b_list_string, "Test failed: sorted list of [8, 13, 21, 30, 16, 17, 1, 15, 7, 16]" \
                                         " != [1, 7, 8, 13, 15, 16, 16, 17, 21, 30]"
    c_list = ListADT()
    c_list.append(8)
    c_list.append(13)
    c_list.append(21)
    c_list.append(30)
    c_list.append(16)
    c_list.append(17)
    c_list.append(1)
    c_list.append(15)
    c_list.append(7)
    c_list.append(16)
    d_list_string = "30\n21\n17\n16\n16\n15\n13\n8\n7\n1\n"
    c_list.sort(True)
    assert str(c_list) == d_list_string, "Test failed: reverse sorted list of [8, 13, 21, 30, 16, 17, 1, 15, 7, 16]" \
                                         " != [30, 21, 17, 16, 16, 15, 13, 8, 7, 1]"


if __name__ == "__main__":
    test_append()
    test_str()
    test_len()
    test_contains()
    test_getitem()
    test_setitem()
    test_eq()
    test_insert()
    test_remove()
    test_delete()
    test_swap()
    test_valid_index()
    test_is_empty()
    test_is_full()
    test_sort()
    print("All tests passing...")

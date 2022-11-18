from task2 import ListADT


def test_append():
    err_list = ListADT()
    for i in range(50):
        err_list.append(i)
    b_list_string = ""
    for j in range(50):
        b_list_string += "{}\n".format(j)
    assert str(err_list) == b_list_string, "Test failed: list of 1 to 50 != list of 1 to 50"
    err_list_two = ListADT()
    for k in range(90):
        err_list.append(k)
    c_list_string = ""
    for m in range(90):
        b_list_string += "{}\n".format(m)
    assert str(err_list_two) == c_list_string, "Test failed: list of 1 to 90 != list of 1 to 90"


def test_insert():
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

    err_list = ListADT()
    for i in range(50):
        err_list.insert(i, i)
    b_list_string = ""
    for j in range(50):
        b_list_string += "{}\n".format(j)
    assert str(err_list) == b_list_string, "Test failed: list of 1 to 50 != list of 1 to 50"
    err_list_two = ListADT()
    for k in range(90):
        err_list.insert(k, k)
    c_list_string = ""
    for m in range(90):
        b_list_string += "{}\n".format(m)
    assert str(err_list_two) == c_list_string, "Test failed: list of 1 to 90 != list of 1 to 90"


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

    err_list = ListADT()
    for i in range(50):
        err_list.append(10)
    for j in range(44):
        err_list.remove(10)
    b_list_string = ""
    for k in range(6):
        b_list_string += "{}\n".format(10)
    assert str(err_list) == b_list_string, "Test failed: removing 44 10's from a list of 50 10's != a list of 6 10's"
    err_list_two = ListADT()
    for m in range(18):
        err_list_two.append(7)
    for n in range(16):
        err_list_two.remove(7)
    c_list_string = ""
    for p in range(2):
        c_list_string += "{}\n".format(7)
    assert str(err_list_two) == c_list_string, "Test failed: removing 16 7's from a list of 18 7's != a list of 2 7's"


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

    err_list = ListADT()
    for i in range(50):
        err_list.append(10)
    for j in range(44):
        err_list.delete(0)
    b_list_string = ""
    for k in range(6):
        b_list_string += "{}\n".format(10)
    assert str(err_list) == b_list_string, "Test failed: delete 44 10's at index 0 from a list of 50 10's" \
                                           "!= a list of 6 10's"
    err_list_two = ListADT()
    for m in range(18):
        err_list_two.append(7)
    for n in range(16):
        err_list_two.delete(0)
    c_list_string = ""
    for p in range(2):
        c_list_string += "{}\n".format(7)
    assert str(err_list_two) == c_list_string, "Test failed: removing 16 7's at index 0 from a list of 18 7's" \
                                               "!= a list of 2 7's"
    e_list = ListADT()
    e_list.append(3)
    e_list.delete(0)
    assert str(e_list) == "", "Test failed: deleting at index 0 for list 3 != empty list"


if __name__ == '__main__':
    test_append()
    test_insert()
    test_remove()
    test_delete()
    print("All tests passing...")

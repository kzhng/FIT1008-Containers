from task6_linked_stack import LinkedStackADT


def test_is_empty():
    a_stack = LinkedStackADT()
    assert a_stack.is_empty(), "Test failed: empty stack empty true != true"
    b_stack = LinkedStackADT()
    b_stack.push(4)
    b_stack.push(6)
    assert not b_stack.is_empty(), "Test failed: non empty stack empty false != false"


def test_push():
    a_stack = LinkedStackADT()
    a_stack.push(35)
    a_stack.push(50)
    assert a_stack.pop() == 50, "Test failed: top of stack is 50 != 50"
    assert a_stack.pop() == 35, "Test failed: top of stack is 35 != 35"


def test_pop():
    try:
        err_stack = LinkedStackADT()
        err_stack.pop()
        assert False, "Test failed: popping an empty list not triggering StopIteration"
    except StopIteration:
        assert True
    a_stack = LinkedStackADT()
    a_stack.push(35)
    a_stack.push(50)
    assert a_stack.pop() == 50, "Test failed: top of stack is 50 != 50"
    assert a_stack.pop() == 35, "Test failed: top of stack is 35 != 35"


if __name__ == '__main__':
    test_is_empty()
    test_push()
    test_pop()
    print("All tests passing...")
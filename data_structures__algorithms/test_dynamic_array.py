import string
import sys

import pytest
from .DynamicArray import DynamicArray


def test_init():
    dynamic_array = DynamicArray()

    assert dynamic_array.capacity == 1
    assert dynamic_array.len == 0
    assert dynamic_array.arr == [None]


def test_init_1():
    dynamic_array = DynamicArray(50)

    assert dynamic_array.capacity == 50
    assert dynamic_array.len == 0
    assert dynamic_array.arr == [None] * 50


def test_init_2():
    with pytest.raises(TypeError) as err:
        DynamicArray("50")

    assert str(err.value) == "Capacity of array need to be: 1) a number 2) greater than 0"


@pytest.mark.parametrize("result", [(3), (12), (25)])
def test_len(result):
    dynamic_array = DynamicArray()
    numbers = [i for i in range(result)]

    for number in numbers:
        dynamic_array.append_element(number)

    assert len(dynamic_array) == result


@pytest.mark.skipif(
    sys.platform == "win32" or sys.version_info < (3, 7),
    reason="Learning purpose: function written for non-windows python 3.7 or higher",
)
def test_getitem():
    dynamic_array = DynamicArray(30)

    dynamic_array.append_element(1, "Hello World!", [2, 3, 5], {"a": ["yupi!", "no!!!!"], "b": (1, 1, 1)})

    assert dynamic_array[0] == 1
    assert dynamic_array[1] == "Hello World!"
    assert dynamic_array[2] == [2, 3, 5]
    assert dynamic_array[3]["a"] == ["yupi!", "no!!!!"]
    assert dynamic_array[3]["b"] == (1, 1, 1)


def test_clear():
    dynamic_array = DynamicArray(20)

    for i in range(10, 30):
        dynamic_array.append_element(i ^ 2)
    dynamic_array.clear()

    assert len(dynamic_array) == 0
    assert dynamic_array[4] is None


def test_set_element():
    dynamic_array = DynamicArray()
    dynamic_array.append_element(1, 2, 3, 4, 5, None)

    dynamic_array.set_element(5, "Hello World!")

    assert dynamic_array[5] == "Hello World!"
    assert len(dynamic_array) == 6

    dynamic_array.set_element(4, None)
    assert dynamic_array[4] is None
    assert len(dynamic_array) == 5

    dynamic_array.set_element(0, "abc")
    assert dynamic_array[0] == "abc"
    assert len(dynamic_array) == 5


def test_remove_at():
    pass


def test_remove():
    dynamic_array = DynamicArray()

    dynamic_array.append_element(1, (1, 1, 1), {2: 30, "abc": 55})
    dynamic_array.remove((1, 1, 1))

    with pytest.raises(ValueError, match="Array does not contain element you want to delete!"):
        dynamic_array.remove([1, 2, 3])
    assert dynamic_array.contains((1, 1, 1)) == -1
    assert len(dynamic_array) == 2


def test_contains():
    letters = list(string.ascii_lowercase)
    dynamic_array = DynamicArray(10)

    for letter in letters:
        dynamic_array.append_element(letter)

    assert dynamic_array.contains("a") == 0
    assert dynamic_array.contains("b") == 1
    assert dynamic_array.contains("z") == 25
    assert dynamic_array.contains(115) == -1


def test__is_out_of_index():
    dynamic_array = DynamicArray()

    with pytest.raises(IndexError, match="Out of array index!"):
        dynamic_array[3]
        dynamic_array[-3]
    with pytest.raises(IndexError, match="Given argument is not a number!"):
        dynamic_array["abbc"]

# ----------------------------------------------------------------------------------------------------------------
# Given a string, develop an algorithm to return the first occurring uppercase letter.
# ----------------------------------------------------------------------------------------------------------------


def find_uppercase_recursive(input_str, index=0):
    if input_str[index].isupper():
        return (index, input_str[index])

    if index == len(input_str) - 1:
        return -1

    return find_uppercase_recursive(input_str, index + 1)


input_str_1 = "AbcadloWFssgdh"
input_str_2 = "fgdjflsskfdghfojlrDdhjlGF"
input_str_3 = "fgdghjkjhgfjlgfdhkdfgkh"

# ----------------------------------------------------------------------------------------------------------------
# Given a string, calculate its length recursively.
# ----------------------------------------------------------------------------------------------------------------


def recursive_str_length(input_str):
    if input_str == "":
        return 0

    return 1 + recursive_str_length(input_str[1:])


# ----------------------------------------------------------------------------------------------------------------
# Given a string, calculate the number of consonants present using recursion.
# ----------------------------------------------------------------------------------------------------------------
vowels = {"a", "e", "i", "o", "u"}


def recursive_count_consonants(input_str):
    if input_str == "":
        return 0

    if (input_str[0].lower() not in vowels) and (input_str[0].isalpha()):
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


# ----------------------------------------------------------------------------------------------------------------
#  Given two numbers, find their product using recursion.
# ----------------------------------------------------------------------------------------------------------------


def recursive_multiply(x, y):
    # prevent from reach maximum recursion depth --> y always should be smaller one
    if y > x:
        return recursive_multiply(y, x)

    if y == 0:
        return 0

    return x + recursive_multiply(x, y - 1)


# ----------------------------------------------------------------------------------------------------------------
#  Add Two Numbers Linked List --> https://leetcode.com/problems/add-two-numbers/discuss/?currentPage=1&orderBy=hot&query=&tag=python3
# ----------------------------------------------------------------------------------------------------------------


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    tmp_val = l1.val + l2.val
    digit, carry_over = tmp_val % 10, tmp_val // 10
    result = ListNode(digit)

    if any((l1.next, l2.next, carry_over)):
        l1 = l1.next if l1.next else ListNode(0)
        l2 = l2.next if l2.next else ListNode(0)
        l1.val += carry_over

        result.next = add_two_numbers(l1, l2)

    return result

"""
TABLE OF CONTENT:
--------------------------
 1) and 2) --> Check if string is anagram - two ways
 3) From given list find all pairs such that, their sum will be equal to given number
 4) Maximum subarray problem
 5) Check if string is palindrome
 6) Reverse words in sentence. E.g: 'Hello, how are you today' --> ['today', 'you', 'are', 'how', ',', 'Hello']
 7) Check if two lists are the same (aka if they have same number of elements and those elements are same (order doesn't matter)) --> [1, 2, 3, 4, 5, 5] and [5, 5, 4, 3, 2, 1] are the same
 8) and 9) --> Unique elements of lists --> take two given lists and return list with unique elements from both lists - two ways
 10) and 11) --> Find  common elements (like intersection of sets) in list --> two ways
 12) and 13) --> Return most frequent element in given list --> two ways
 14) Check if all chars in given string are unique (occurred at most once)
 15) and 16 Return non-repeating chars in given string --> two ways
 17) We wish to determine the optimal way in which to assign tasks to workers. Each worker must work on exactly two tasks. Tasks are independent and each task takes a fixed amount of time --> optimal task assignment
 18) Destination city --> https://leetcode.com/problems/destination-city/
 19) How Many Numbers Are Smaller Than the Current Number --> https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
 20) Binary Search --> https://leetcode.com/problems/binary-search/
 21) Longest palindrome --> https://leetcode.com/problems/longest-palindrome/
 22) Design Browser History --> https://leetcode.com/problems/design-browser-history/
 23) Two sum --> https://leetcode.com/problems/two-sum/
 24)  Longest Substring Without Repeating Characters --> https://leetcode.com/problems/longest-substring-without-repeating-characters/
 25) Plus one --> https://leetcode.com/problems/plus-one/
 26) Single Number (power of XOR) --> https://leetcode.com/problems/single-number/
 27) Longest Common Prefix --> https://leetcode.com/problems/longest-common-prefix/
 28) Maximum Depth of Binary Tree --> https://leetcode.com/problems/maximum-depth-of-binary-tree/
 29) Roman Numbers
--------------------------
"""

# 1)
def is_anagram(str_1, str_2):
    """Check if two given string are anagram.
    Angaram -> a word, phrase, or name formed by rearranging the letters of another. E.g.: 'Tom Marvolo Riddle' -> 'i am lord voldemort'

    Args:
        str_1 (string): given string (first) to compare
        str_2 (string): given string (second) to compare

    Returns:
        boolean: boolean value according to result of comparision
    """
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    return sorted(str_1) == sorted(str_2)


# 2)
def is_anagram_via_dict_count(str_1, str_2):
    """Check if two given string are anagram by using dictionary

    Args:
        str_1 (string): given string (second) to compare
        str_2 (string): given string (second) to compare

    Returns:
        boolean: boolean value according to result of comparision
    """
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    if len(str_1) != len(str_2):  # necessary condition --> anagram need to have the same number of letters
        return False

    count = {}
    for char in str_1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in str_2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1

    for key in count:
        if count[key] != 0:
            return False

    return True


# print(is_anagram('Tom Marvolo Riddle', 'i am lord voldemort'),
# is_anagram_via_dict_count('Tom Marvolo Riddle', 'i am lord voldemort'))'''

# 3)
def pair_sum(list, sum):
    """Return set of tuples of all pairs, that give given sum when added.
    Example: pair_sum([0, 1, 2, 3, 4, 5], 5) will return: {(2, 3), (1, 4), (0, 5)}

    Args:
        list (list): list of numbers (int or float) from which pairs will be search
        sum (number (integer or float)): the number which is a result of addition searched pairs

    Raises:
        IndexError: Given list need to have at least 2 elements

    Returns:
        set: Set of tuples which meet given criteria. If such pairs don't exist empty set will be returned
    """
    if len(list) < 2:
        raise IndexError("Given list has to small input")

    already_seen = set()
    results = set()  # order doesn't matter --> 5 = (1, 4) or (4, 1) are the same

    for number in list:
        looking_number = sum - number

        if looking_number in already_seen:
            results.add((min(looking_number, number), max(looking_number, number)))  # add one tuple with 2 elements
        else:
            already_seen.add(number)

    return results


# print(pair_sum([-5, 0, 1, 2, 3, 4, 5, 10], 5))

# 4)
def largest_sum(list):
    """Take given list of numbers and return typle: largest sum of contiguous sublist, and actual sublist, which generate this sum

    Args:
        list (list): Given list of numbers (int or float) from which largest sum will be calculated

    Raises:
        IndexError: Given list need to have at least 1 elements

    Returns:
        tuple --> (sublist, max_sum)
    """
    if len(list) < 1:
        raise IndexError("Given list has to small input")

    max_sum = current_sum = 0
    current_start_index = current_end_index = 0
    max_start_index = max_end_index = 0

    # below algorithm (Kadane's algorithm) work well unless all elements are negative numbers (require manuall intervention --> see 'intervention line')
    # General idea: iterate through loop and add every element - whenever sum is below 0 current subarray is for sure not the searched one.
    # Trace current sum (temporary variable) and keep comparing (after every iteration) to so far the biggest sum
    # If you got new biggest sum -> also write down it's beggining and end (indexes) - to do so, you need to track current indexes (temporary variables)
    for current_end_index, number in enumerate(list):
        if (
            current_sum < 0
        ):  # need to reset current traced index and start traced current one => I should start traced from current end index
            current_start_index = current_end_index
            current_sum = number
        else:
            current_sum += number
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = current_start_index
            max_end_index = (
                current_end_index + 1
            )  # list[a:b] -> give elements from a index to b - 1; index a = [1, 2, 3, 4], a[0:2] = [1, 2]

    largest_sum_sublist = list[max_start_index:max_end_index]
    if (
        len(largest_sum_sublist) == 0
    ):  # 'intervention line' at this stage it means that all numbers in list are negative => the biggest number(from all negative numbers) is max_sum (one-element subarray)
        return ([max(list)], max(list))

    return (max_sum, largest_sum_sublist)


# print(largest_sum([-2, -4, -7, -2, -2, -1]))

# 5)
def is_palindrome(str):
    """Check if given string is palindrome.
    palindrome -> a word, phrase, number or sequence of words that reads the same backward as forward. Punctuation and spaces between the words or lettering is allowed.
    E.g.: 'Anna', 'My gym' ('Myg ym')

    Args:
        str (string): given string to check

    Returns:
        boolean: boolean value according to result of check
    """
    # Because "punctuation and spaces between the words or lettering is allowed I need to make all lowercase and eliminate all spaces
    str = str.lower()
    str = [elem.replace(" ", "") for elem in str]
    str = "".join(str)  # cast list to string

    return str[::-1] == str


# 6)
def words_in_reverse_order(sentence):
    """Return words from given sentence in reverse order. Remember that a word is separated by space, so:
    'Hello, how are you today?' --> 'Today? you are how hello,'
    'Hello , how are you today ?' --> '? today you are how , hello'

    Args:
        sentence (srting): given sentence

    Returns:
        string: words in reverse order
    """
    sentence = list(sentence.lower().split())
    sentence.reverse()
    return " ".join(sentence).capitalize()


# print(words_in_reverse_order("Hello, how are you today?"))
# print(words_in_reverse_order("Hello , how are you today ?"))

# 7)
def are_lists_same(list_1, list_2):
    """Check if two given list have same elements (necessary condition -> lists need to have the same number of elements - it is like equivalent and equal set from set theory;
    equal requires equivalent, but not vice versa). So if function returns True lists have same "cardinality", but if returns False - lists may or may not have same "cardinality".

    Args:
        list_1 (list): given list (first) to compare
        list_2 (list): given list (second) to compare

    Returns:
        boolean: boolean value according to result of check
    """
    result = 0
    for number in list_1 + list_2:  # using properties of bitwise XOR
        result ^= number

    if result == 0:
        return True
    else:
        return False


# print(are_lists_same([1, 2, 3, 4, 5, 6], [6, 4, 2, 1, 5, 3]))
# print(are_lists_same([], []))

# 8)
def unique_elements(list_1, list_2):
    """Return list which contains these elements which appear only in one from both given list.
    Example: [0, 1, 2, 3, 4, 5] and [3, 4, 5, 6, 7] will return [0, 1, 2, 6, 7]

    Args:
        list_1 (list): given list (first) to compare
        list_2 (list): given list (second) to compare

    Returns:
        list: list with unique elements from each list
    """
    sum_list = list_1 + list_2

    results = [elem for elem in sum_list if (elem not in list_1) or (elem not in list_2)]

    return results


# print(unique_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7]))
# print(unique_elements([], ["skok", "dal"]))


# 9)
def unique_elements_v2(list_1, list_2):
    # Same as above ->  ""... which contains these elements which appear only in one from both given list" - exact definition of symetric difference from set theory
    # (set that containl elements such that they belong only to A or belong only to B, but not in their intersection)

    return list(set(list_1).symmetric_difference(list_2))


# print(unique_elements_v2([1, 1, 2, 2, 3, 4, 4, 5, 6], [3, 4, 7, 8, 8]))
# print(unique_elements_v2("Winter is coming!", "coming!"))

# 10)
def arrays_common_elements(list_1, list_2):
    list_1 = sorted(set(list_1))  # sorted() always return a list
    list_2 = sorted(set(list_2))
    current_index_l1 = 0
    current_index_l2 = 0
    results = []

    while current_index_l1 < len(list_1) and current_index_l2 < len(list_2):
        if list_1[current_index_l1] == list_2[current_index_l2]:
            results.append(list_1[current_index_l1])
            current_index_l1 += 1
            current_index_l2 += 1

        elif list_1[current_index_l1] > list_2[current_index_l2]:
            current_index_l2 += 1

        else:  # list_1[current_index_l1] < list_2[current_index_l2]
            current_index_l1 += 1

    return results


# print(arrays_common_elements([1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 9, 10], [7, 5, 4, 3, 10]))

# 11)
def arrays_common_elements_more_pythonic_way(list_1, list_2):
    return [element for element in set(list_1) if element in set(list_2)]
    # return list(set(list_1).intersection(list_2))


# print(arrays_common_elements_more_pythonic_way([1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 9, 10], [7, 5, 4, 3, 10]))

# test code efficency for 10) vs 11)
import timeit

SET_UP = """
import random

list_1 = [random.randint(0, 10000) for i in range(1000000)]
list_2 = [random.randint(0, 10000) for i in range(1000000)]
"""
TEST_CODE_1 = """
def arrays_common_elements():
    global list_1, list_2
    list_1 = sorted(set(list_1))
    list_2 = sorted(set(list_2))
    current_index_l1 = 0
    current_index_l2 = 0
    results = []

    while current_index_l1 < len(list_1) and current_index_l2 < len(list_2):
        if list_1[current_index_l1] == list_2[current_index_l2]:
            results.append(list_1[current_index_l1])
            current_index_l1 += 1
            current_index_l2 += 1

        elif list_1[current_index_l1] > list_2[current_index_l2]:
            current_index_l2 += 1

        else:  # list_1[current_index_l1] < list_2[current_index_l2]
            current_index_l1 += 1

    return results
"""
TEST_CODE_2 = """
def arrays_common_elements_more_pythonic_way(list_1, list_2):
    return [element for element in set(list_1) if element in set(list_2)]
"""
# print(f"Less pythonic code run in: {timeit.timeit(stmt=TEST_CODE_1, setup=SET_UP, number=10000000)}")
# print(f"More pythonic code run in: {timeit.timeit(stmt=TEST_CODE_2, setup=SET_UP, number=10000000)}")

# 12)
def most_frequent_element_in_list(list):
    """Return most frequent occurred element in the list"""
    chars_count = {}
    max_count = 0
    most_frequent_element = None

    for element in list:
        if element in chars_count:
            chars_count[element] += 1
        else:
            chars_count[element] = 1

        if chars_count[element] > max_count:
            max_count = chars_count[element]
            most_frequent_element = element

    return most_frequent_element


# print(most_frequent_element_in_list([1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8]))

# 13)
from collections import Counter


def most_frequent_element_in_list_with_counter(list):
    # Same as above - take shortcuts with Counter()
    occurence_count = Counter(list)
    return occurence_count.most_common(1)[0][0]  # most_common() method return list of
    # tuples (quantity of this list is specify by given argument (1 in this case) (element,count_number)


# print(most_frequent_element_in_list_with_counter([1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 7]))

# 14)
def is_all_chars_unique(string):
    """Check if all chars in given string are unique (occurred at most once)

    Args:
        string (string): given string

    Returns:
        boolean: boolean value according to result of check
    """
    string = string.replace(" ", "").lower()
    return len(string) == len(set(string))


# print(is_all_chars_unique("Eviva l'arte!"))

# 15)
def non_repeating_chars(string):
    """Return a list of non-repeating chars in given string.

    Args:
        string (string): given string

    Returns:
        list: list of non-repeating chars
    """
    string = string.replace(" ", "").lower()
    chars_count = {}
    results = []

    for char in string:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    for char in chars_count:
        if chars_count[char] == 1:
            results.append(char)

    return results


# print(non_repeating_chars("Eviva l'arte!"))

# 16)
from collections import Counter


def non_repeating_chars_with_counter(string):
    string = string.replace(" ", "").lower()
    string_counter = Counter(string)
    return [char for char, occurence_number in string_counter.items() if occurence_number == 1]


# print(non_repeating_chars_with_counter("Eviva l'arte!"))

# 17)
"""
A = [1, 9, 12, 17, 3, 6, 2, 5, 18, 7]
A.sort()
for i in range(len(A) // 2):
    print(A[i], "-->", A[~i], "; sum:", (A[i] + A[~i]), sep=" ")
"""

# 18)
from typing import List


def destination_city(paths: List[List[str]]) -> str:
    outgoing_counts = {}
    for cities in paths:
        depature, destination = cities
        outgoing_counts[depature] = outgoing_counts.get(depature, 0) + 1
        outgoing_counts[destination] = outgoing_counts.get(destination, 0)

    for city in outgoing_counts:
        if outgoing_counts[city] == 0:
            return city


# destination_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])

# 19)
from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    sort_nums = sorted(nums, reverse=True)
    counts_smaller_number = {}
    results = []

    for i in range(len(sort_nums) - 1):
        current_num = sort_nums[i]
        next_num = sort_nums[i + 1]
        if next_num < current_num:
            remaining_nums = len(sort_nums) - (i + 1)
            counts_smaller_number[current_num] = remaining_nums

    counts_smaller_number[sort_nums[-1]] = 0

    for num in nums:
        results.append(counts_smaller_number[num])

    return results


# print(smaller_numbers_than_current([2, 5, 1, 6, 3]))

# 20)
from typing import List


def search(nums: List[int], target) -> int:
    def binary_search(st_index, end_index, nums):
        if st_index <= end_index:
            mid_index = (st_index + end_index) // 2

            if nums[mid_index] == target:
                return mid_index

            elif nums[mid_index] < target:
                return binary_search(mid_index + 1, end_index, nums)

            elif nums[mid_index] > target:
                return binary_search(st_index, mid_index - 1, nums)
        else:
            return -1

    return binary_search(0, len(nums) - 1, nums)


# a = [x for x in range(100000000)]
# print(search(a, 1000))

# 21)
from typing import List


def longest_palindrome(s: str) -> int:
    result = 0
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    is_odd_present = False
    for char in char_count:
        if char_count[char] % 2 == 0:
            result += char_count[char]
        else:
            result += char_count[char] - 1
            is_odd_present = True

        if is_odd_present:
            result += 1

    return result


# 22)
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self._current_index = 0

    def visit(self, url: str):
        self._current_index += 1
        self.history = self.history[0 : self._current_index]  # clears foward history
        self.history.append(url)

    def back(self, steps: int) -> str:
        self._current_index = max(0, self._current_index - steps)

        return self.history[self.current_index]

    def foward(self, steps: int) -> str:
        self.current_index = min(len(self.history) - 1, self.current_index + steps)

        return self.history[self._current_index]


# 23)
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    already_seen = {}

    for i, num in enumerate(nums):
        if (target - num) in already_seen:
            return (i, already_seen[target - num])
        elif num not in already_seen:
            already_seen[num] = i


# 24)
def length_of_longest_substring(s: str) -> int:
    already_seen = {}
    current_substr_start = 0
    current_substr_length = 0
    longest_substr = 0

    for i, char in enumerate(s):
        if char in already_seen and already_seen[char] >= current_substr_start:
            current_substr_start = already_seen[char] + 1
            current_substr_length = i - already_seen[char]
            already_seen[char] = i

        else:
            already_seen[char] = i
            current_substr_length += 1

            if current_substr_length > longest_substr:
                longest_substr = current_substr_length

    return longest_substr


# 25)
from typing import List


def plus_one(nums: List[int]):
    return [int(x) for x in str(int("".join([str(x) for x in nums])) + 1)]


# 26)
from typing import List


def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num

    return num


# 27)
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    current_prefix = strs[0]
    current_prefix_len = len(current_prefix)

    for world in strs[1:]:
        while current_prefix != world[:current_prefix_len]:
            current_prefix = current_prefix[:-1]
            current_prefix_len -= 1

            if current_prefix_len == 0:
                return ""

    return current_prefix


# 28)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maximum_depth_of_binary_tee(self, root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(maximum_depth_of_binary_tee(root.left), maximum_depth_of_binary_tee(root.right))


# 29)
def to_roman(num: int) -> str:
    TO_ROMAN = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    result = ""

    for arabic_num, roman_char in TO_ROMAN.items():
        result += roman_char * (num // arabic_num)
        num %= arabic_num

    return result


def from_roman(roman: str) -> int:
    FROM_ROMAN = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    result = 0
    index = 0

    for roman_char, arabic_num in FROM_ROMAN.items():
        while roman[index : index + len(roman_char)] == roman_char:
            result += arabic_num
            index += len(roman_char)

    return result

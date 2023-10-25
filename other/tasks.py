from decimal import Decimal

def show_numbers(): #zad_3
    decimal_numbers = [Decimal(x / 10.0) for x in range(20, 56, 5)]
    print(decimal_numbers)

def check_list(list, n):  #zad_2
    complete_list = set(x for x in range(1, (n+1)))

    missing_numbers = complete_list - set(list)
    print(sorted(missing_numbers))

def codes_generator(code_1, code_2):  #zad_1
    code_1, code_2 = code_1.split('-'), code_2.split('-')
    code_1, code_2 = int(code_1[0] + code_1[1]), int(code_2[0] + code_2[1])

    for x in range((code_1 + 1), code_2):
        print(f"{x // 1000}-{str(x % 1000).rjust(3, '0')}")

print('\n')
show_numbers()
print('\n')
check_list([1,2,3,4,5,6,9], 12)
print('\n')
codes_generator('83-150','84-330')






-----------------------------------------------------------------------------------------------------------------------

#zad_1
def solution(num_1, num_2):
    num_1, num_2 = str(num_1), str(num_2)
    iterator = 0
    results = []

    while iterator < len(num_2):
        iterator = num_2.find(num_1, iterator)
        if iterator == -1:
            break
        else:
            iterator += len(num_1)
            results.append(iterator)

    if not results:
        results.append(-1)

    print(results)

#zad_2
def solution_1(num_1, num_2, array):
        num_1_occurs = 0
        num_2_occurs = 0
        result = 0

        for i in range(0, len(array)):
            if array[i] == num_1:
                num_1_occurs += 1
            if array[i] == num_2:
                num_2_occurs += 1
            if num_1_occurs == num_2_occurs:
                result = i
            else:
                result = -1

        print(result)

    solution_1(0, 1, [0, 0, 0, 1, 1, 1, 2])

#zad_3
def amplitude(array):
    if len(array) < 2:
        return 0
    else:
        return max(array) - min(array)


def solution(array):
    start_index = 0
    end_index = start_index + 1
    solution = 0
    array.sort()

    while end_index <= len(array):
        temporary = array[start_index:end_index]
        if amplitude(temporary) <= 1:
            end_index += 1
            if len(temporary) > solution:
                solution = len(temporary)
        else:
            start_index = end_index
            end_index += 1

    return solution

'''
from collections import defaultdict

def longestQuasiConstantSubseqLength(array):
  occurs_count = defaultdict(int)
  for integer in array:
    occurs_count[integer] += 1
    occurs_count[integer + 1] += 1
  return max(occurs_count.values() or [0]) #handle empty list ([0] -> means 1-element array, namely [ 0 ]) 

array = []

print(longestQuasiConstantSubseqLength(array))

'''


print(solution([2, 6, 8, 10]))


------------------------------------------------------------------------------------------------------------------------------------
#function takes the value of any integer - and check what maximum value can be obtain if remove digit 5 (only one at time!)
# variation ---> https://www.geeksforgeeks.org/largest-number-possible-after-removal-of-k-digits/
def test(N):
    number_str = str(N)
    indexes = []
    tmp_values = []

    for index, value in enumerate(number_str):
        if value == "5":
            indexes.append(index)

    for index in indexes:
        number_list = [number_str[i] for i in range(len(number_str)) if i != index]
        tmp_value = int("".join(number_list))
        tmp_values.append(tmp_value)
    
    return max(tmp_values)
        

print(test(-50))

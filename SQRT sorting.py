import math

def sqrt_sort(numbers):
    """Step by step function:
    1) Arrival of the list
    2) Sqrt the list
    3) Sort the list
    4) Undo Sqrt and return sorted list"""
    
    step1 = sqrt_list(numbers)
    step2 = sort_list(step1)
    step3 = undo_sqrt_list(step2)
    return step3

def sort_list(numbers):
    """Function for sorting the given list of numbers, dividing the provided numbers
    into two list: Numbers greater than the pivot goes to one list, numbers lower than the pivot
    goes to the other list. Then, recursion until the lenght of the list equals 1"""
    
    elem_greater = []
    elem_lower = []

    if len(numbers) <= 1:  # If the list given is 1 or less, stops the sorting method
        return numbers
    else:  # Taking the last element away and storing it as a pivot
        pivot = numbers.pop()

    for elem in numbers:
        if elem < pivot:
            elem_greater.append(elem)
        else:
            elem_lower.append(elem)

    # Recursion 
    return sort_list(elem_lower) + [pivot] + sort_list(elem_greater)


def sqrt_list(numbers):
    """Function for swaping all elements in the list for
    his square root value"""
    elem_rooted = []
    for i in numbers:
        elem_rooted.append(math.sqrt(i))

    return elem_rooted


def undo_sqrt_list(numbers):
    """Function for restablish the original value of the
    elements"""
    elem_unrooted = []
    for i in numbers:
        unrooted_num = int(i * i)
        elem_unrooted.append(unrooted_num)

    return elem_unrooted


test_list = [625, 71, 25, 16, 4, 26, 36, 58, 1, 49, 256]

print(sqrt_sort(test_list))

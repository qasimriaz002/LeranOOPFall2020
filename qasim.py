from typing import List


def count_evens(values: List[List[int]]) -> List[int]:
    """Return a list of counts of even numbers in each of the inner lists
    of values.

    # >>> count_evens([[10, 20, 30]])
    [3]
    # >>> count_evens([[1, 2], [3], [4, 5, 6]])
    [1, 0, 2]
    """
    evenList = []
    for sublist in values:
        count = 0
        for eachValue in sublist:
            if eachValue % 2 == 0:
                count = count + 1
        evenList.append(count)
    return evenList

x = [[1, 2], [3], [4, 5, 6]]
print(count_evens(x))
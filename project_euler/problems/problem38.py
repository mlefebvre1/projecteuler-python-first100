from functools import reduce

from project_euler.arithmetic.arithmetic import pandigital_validation

from project_euler.utils.timeit import timeit


@timeit
def problem38():
    """
    Pandigital multiples
    Problem 38

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
    product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
    which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
    with (1,2, ... , n) where n > 1?

    if the number of digits is n, solutions will be found by concatenating at least 6-n multiplied numbers :
        1 : 5
        2 : no solutions
        3 : 3
        4 : 2
        5 > : no solutions
    """
    max_n = 10000
    best = 0
    for n in range(1, max_n):
        number = reduce(lambda out, digit: out + str(n * digit), range(1, 7 - len(str(n))), "")
        if pandigital_validation(number, 1, 9) and int(number) > best:
            best = int(number)
    return best


if __name__ == "__main__":
    problem38()

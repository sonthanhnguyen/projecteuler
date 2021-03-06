"""
    Project Euler 43: Sub-string divisibility

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each
    of the digits 0 to 9 in some order, but it also has a rather interesting sub-string
    divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools
import time

PRIME_LIST = [2, 3, 5, 7, 11, 13, 17]


def are_sub_strings_divisible(string):
    """
    Check if sub strings created out of an input string are divisible with the condition above

    :param string: the input string to test
    :return: True if all sub strings are divisible with such condition, False otherwise.
    """
    for index, value in enumerate(PRIME_LIST):
        if int(string[index + 1: index + 4]) % value != 0:
            return False

    return True


def find_the_sum(string):
    """
    Return sum of all 0 to 9 pandigital numbers with divisible sub-strings

    :param string: contains all digits from 0 to 9, each appears once, used as inputs
     to find 0 to 9 pandigital numbers
    :return: the sum
    """
    the_sum = 0

    # Search for all 10-digit pandigital numbers
    for perm in itertools.permutations(string):
        # Ignore '0' in the beginning as that string does not form 10-digit number,
        # hence not 'that' pandigital
        if perm[0] == '0':
            continue

        temp = ''.join(list(perm))

        # Check for the divisibility property
        if are_sub_strings_divisible(temp):
            the_sum += int(temp)

    return the_sum


def main():
    """
    Test
    """
    start_time = time.time()
    result = find_the_sum('0123456789')
    print("The result is {0}, found in {1} seconds"
          .format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

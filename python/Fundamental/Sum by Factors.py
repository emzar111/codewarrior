from math import sqrt
from collections import defaultdict


def simple_numbers(number):
    lst = [2, 3, 5]

    if number == 2:
        lst = [2]
        return lst
    if number == 3:
        lst = [2, 3]
        return lst

    for i in range(5, number + 1, 2):
        if i % 5 == 0:
            continue
        for j in range(3, i + 1):
            if j > int(sqrt(i)):
                lst.append(i)
                break
            if i % j == 0:
                break
    return lst


def sum_for_list(lst):
    m = 0
    result = []
    for i in lst:
        if m < abs(i):
            m = abs(i)
    for i in simple_numbers(m):
        sum_lst = 0
        div_check = 0
        for j in lst:
            if j % i == 0:
                div_check = 1
                sum_lst += j
        if div_check:
            result.append([i, sum_lst])
    return result

'''
Best solution!!!
def sum_for_list(lst):
    factors = {i for k in lst for i in xrange(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

'''
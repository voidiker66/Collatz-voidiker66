#!/usr/bin/env python3

# ------------------
# collatz/Collatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ------------------

from typing import IO, List
from known_cache import known_cache_1000

# known_cache_1000 is a hard coded CACHE
# the MCL for ranges 1-999, 1000-1999, 2000-2999, etc
# are in a set that we can reference
# all numbers in known_cache were calculated
# using the less efficient version of this code

# ------------
# collatz_read
# ------------

def collatz_read(string: str) -> List[int]:
    """
    read two ints
    string a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    array_ouput = string.split()
    return [int(array_ouput[0]), int(array_ouput[1])]

# ------------
# collatz_eval
# ------------


# CACHE for the get_cycles
# reduces computations by storing known values
CACHE = {}

# recursive function that finds cycle length
# if value in CACHE, returns CACHE value
# if even, divide by two
# if odd, multiply by three and add one
# if one, return one

def get_cycles(i: int):
    """
    gets the cycle length of a single integer i
    """
    # if in CACHE, we already know the answer
    if i in CACHE:
        return CACHE[i]
    # MCL of 1 and 2 are 1 and 2 respectively
    if i == 1 or i == 2:
        return i
    # if not known, calculate and store in CACHE
    if i % 2 == 0:
        CACHE[i] = int(get_cycles(int(i/2)) + 1)
        return CACHE[i]
    CACHE[i] = int(get_cycles(int((i*3)+1)) + 1)
    return CACHE[i]

def get_max_cycle_length(start: int, end: int):
    """
    gets the max cycle length between
    two integers start and end
    """
    # iterate from start to end and return the MCL
    # helper func because defined multiple times
    # inside collatz_eval
    res = 0
    for iteration in range(start, end+1):
        temp = get_cycles(int(iteration))
        if temp > res:
            res = temp

    return res

def collatz_eval(i: int, j: int) -> int:
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>

    # need larger number to be j
    if i > j:
        temp = i
        i = j
        j = temp

    # if diff < 1000, cant use known_cache_1000
    # because we can't assume MCL of known_cache section
    # is in i-j range
    if j-i < 1000:
        return get_max_cycle_length(i, j)

    # since known_cache_1000 gets MCL of every 1000
    # and we don't want to calculate what we already know
    # we need to find lowest 1000 above lower bound and
    # highest 1000 lower than upper bound
    start = int(i/1000)
    end = int(j/1000)

    # low bound is the MCL of the lower bound
    # high bound is the MCL of the upper bound
    low_bound = get_max_cycle_length(i, int((start+1)*1000))
    high_bound = get_max_cycle_length(int(end*1000), j)

    # known bound is the MCL that we can learn
    # from reading known_cache_1000
    known_bound = 0
    # need to increment start
    # if not, known bound will include below lower bound
    start += 1
    # if start < end, no information can be learned
    # from known_cache because we can't assume
    # MCL of what we know is in i-j range
    if start < end:
        while start != end:
            if known_cache_1000[start] > known_bound:
                known_bound = known_cache_1000[start]
            start += 1

    # return the highest MCL of the three options
    if low_bound >= high_bound:
        if low_bound >= known_bound:
            return low_bound
        return known_bound
    if high_bound >= known_bound:
        return high_bound
    return known_bound




# -------------
# collatz_print
# -------------

def collatz_print(write: IO[str], start: int, end: int, result: int) -> None:
    """
    print three ints
    write a writer
    start the beginning of the range, inclusive
    end the end       of the range, inclusive
    result the max cycle length
    """
    write.write(str(start) + " " + str(end) + " " + str(result) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve(read: IO[str], write: IO[str]) -> None:
    """
    r a reader
    w a writer
    """
    for input_array in read:
        start, end = collatz_read(input_array)
        result = collatz_eval(start, end)
        collatz_print(write, start, end, result)

#!/usr/bin/env python3

# ------------------
# collatz/Collatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ------------------

from typing import IO, List
from known_cache import known_cache_1000

# ------------
# collatz_read
# ------------

def collatz_read (s: str) -> List[int] :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------



# cache for the getCycles
# reduces computations by storing known values
cache = {}

# recursive function that finds cycle length
# if value in cache, returns cache value
# if even, divide by two
# if odd, multiply by three and add one
# if one, return one

def getCycles(i: int):
    if i in cache:
        return cache[i]
    if i == 1 or i == 2:
        return i
    if i % 2 == 0:
        cache[i] = int(getCycles(int(i/2)) + 1)
        return cache[i]
    cache[i] = int(getCycles(int((i*3)+1)) + 1)
    return cache[i]

def getMaxCycleLength(i: int, j: int):
    res = 0
    for x in range(i, j+1):
        temp = getCycles(int(x))
        if temp > res:
            res = temp

    return res

def collatz_eval (i: int, j: int) -> int :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    if i > j:
        temp = i
        i = j
        j = temp
    
    # if diff < 1000, cant use known_cache_1000
    if (j-1 < 1000):
        return getMaxCycleLength(i, j)

    start = int(i/1000)
    end = int(j/1000)

    low_bound = getMaxCycleLength(i, int((start+1)*1000))
    high_bound = getMaxCycleLength(int(end*1000), j)

    known_bound = 0
    while start != end:
        if known_cache_1000[start] > known_bound:
            known_bound = known_cache_1000[start]
        start += 1

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

def collatz_print (w: IO[str], i: int, j: int, v: int) -> None :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")
    #w.write(str(v) + ", ")

# -------------
# collatz_solve
# -------------

def collatz_solve (r: IO[str], w: IO[str]) -> None :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python

# ---------------------
# collatz/RunCollatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ---------------------

# -------
# imports
# -------

from sys import stdin, stdout
from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(stdin, stdout)

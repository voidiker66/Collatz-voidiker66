#!/usr/bin/env python3

# ----------------------
# collatz/TestCollatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ----------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 11)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 300)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 411)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 1900)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 11\n100 200 300\n201 210 411\n900 1000 1900\n")

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    main()

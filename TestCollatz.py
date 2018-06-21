#!/usr/bin/env python

# ----------------------
# collatz/TestCollatz.py
# Copyright (C) 2018
# Glenn P. Downing
# ----------------------

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Testing class for this assignment
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
        tests the collatz_read function
        returns two ints from string
        """
        input_var = "1 10\n"
        start, end = collatz_read(input_var)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    def test_eval_5(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(1, 1)
        self.assertEqual(result, 1)

    def test_eval_6(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(1, 2)
        self.assertEqual(result, 2)

    def test_eval_7(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(54310, 533814)
        self.assertEqual(result, 470)

    def test_eval_8(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(253809, 70626)
        self.assertEqual(result, 443)

    def test_eval_9(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(1, 1000000)
        self.assertEqual(result, 525)

    def test_eval_10(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(3001, 4001)
        self.assertEqual(result, 238)

    def test_eval_11(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(9040, 1040)
        self.assertEqual(result, 262)

    def test_eval_12(self):
        """
        tests if eval returns the correct
        MCL for the range provided
        """
        result = collatz_eval(1, 3999)
        self.assertEqual(result, 238)

    # -----
    # print
    # -----

    def test_print(self):
        """
        tests the print function
        important for diff check
        """
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        tests if I can solve multiple inputs in order
        """
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----


if __name__ == "__main__":
    # pragma: no cover
    main()

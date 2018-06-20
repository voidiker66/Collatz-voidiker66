from random import randint

with open("uint_test.py", 'w') as f:
	f.write("from io       import StringIO\nfrom unittest import main, TestCase\nfrom Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve\n\n")
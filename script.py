with open("RunCollatz.in", 'w') as f:
	x = 0
	y = 999
	while x != 1000000:
		f.write(str(x) + " " + str(y) + "\n")
		x += 1000
		y += 1000
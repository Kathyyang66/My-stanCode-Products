"""
File: coin_flip_runs.py
Name: Kathy Yang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: Manufacturing code to calculate the number of run.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	result_1 = r.randint(1, 2)
	result_2 = 0
	ans = ''
	run_count = 0
	is_in_record = False
	while True:
		if result_1 == 1:
			ans += 'H'
		else:
			ans += 'T'
		if result_1 == result_2:
			if not is_in_record:
				run_count += 1
				is_in_record = True
		else:
			is_in_record = False
		result_2 = result_1
		if run_count == num_run:
			break
		result_1 = r.randint(1, 2)
	print(ans)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

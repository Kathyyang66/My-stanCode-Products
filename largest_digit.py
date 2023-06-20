"""
File: largest_digit.py
Name: Kathy Yang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, giving numbers.
	:return: int, the bigger number.
	"""
	if n < 0:
		n = -n
	if n//10 == 0:
		return n
	else:
		current = n
		unit = current % 10
		last_second_one = (current-unit)//10
		a = find_largest_digit(last_second_one)
		return max(unit, a)


if __name__ == '__main__':
	main()

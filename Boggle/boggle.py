"""
File: boggle.py
Name: Kathy Yang
----------------------------------------
According to the letters that user input, searching any kinds of words which length longer than 4 in dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	According to the letters that user input, searching any kinds of words which length longer than 4 in dictionary.
	"""
	start = time.time()
	a = []
	dict_lst = read_dictionary()
	all_lst = []
	for i in range(4):
		n = input(f'{i+1} rows of letters: ').lower().split(' ')
		for ch in n:
			if len(ch) != 1:
				print('Illegal input')
				return
		all_lst.append(n)
	for i in range(4):
		for j in range(4):
			used_index = [(i, j)]
			ans = all_lst[i][j]
			boggle(ans, i, j, used_index, all_lst, dict_lst, a)
	print(f"There are {len(a)} words in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(ans, x, y, used_index, all_lst, dict_lst, a):
	"""
	:param ans: string, used to be a container
	:param x: location for x, used to indicate a spot.
	:param y: location for y, used to indicate a spot.
	:param used_index: list, judging if certain location has been looped.
	:param all_lst: list, used to accommodate the data that user input
	:param dict_lst: list, the list includes all the correct token words.
	:param a:list, judging if a word exists in all_lst or not.
	"""
	if ans in dict_lst:
		if ans not in a:
			print(f'Found "{ans}"')
			a.append(ans)
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if 0 <= i+x < 4 and 0 <= j+y < 4 and (i+x, j+y) not in used_index:
				if i+x != x or y+j != y:
					# choose
					used_index.append((i+x, j+y))
					ans += all_lst[i+x][j+y]
					# explore
					if has_prefix(ans, dict_lst):
						boggle( ans, x+i, y+j, used_index, all_lst, dict_lst, a)
					# un-choose
					used_index.pop()
					ans = ans[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r')as f:
		for line in f:
			if len(line.strip()) >= 4:
				lst.append(line.strip())
	return lst


def has_prefix(sub_s, dict_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in dict_lst:
		if ch.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

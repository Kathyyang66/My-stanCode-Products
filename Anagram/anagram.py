"""
File: anagram.py
Name: Kathy Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: When user key in a word, searching words in same elements and spelling in different way.
    """
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            start = time.time()
            lst = read_dictionary(s)
            ans_lst = find_anagrams(s, lst)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    lst = []
    with open(FILE, 'r')as f:
        for line in f:
            tokens = line.strip().split()
            for token in tokens:
                if len(s) == len(token):
                    lst.append(token)
    return lst


def find_anagrams(s, lst):
    """
    :param s:string, the word that user give.
    :param lst: list, the list which stores token words without moving to new line function.
    """
    long = len(s)
    anagrams = []
    find_anagrams_helper(s, anagrams, "", lst, long)
    print(len(anagrams), " anagrams: ", anagrams)
    return anagrams


def find_anagrams_helper(s, current_l, current_s, lst, long):
    """
    :param s:string, the word that user give.
    :param current_l: list, if the word appears in dictionary, putting into current_l.
    :param current_s: sting, if partial words exist in dictionary, appending to current string.
    :param lst: list, the list which stores token words without moving to new line function.
    :param long: original len(s), making the variable to ensure len(s) wouldn't be changed.
    """

    if len(current_s) == long and current_s in lst:
        if current_s not in current_l:
            current_l.append(current_s)
            print("Searching ...")
            print("Found: "+current_s)
    else:
        for i in range(len(s)):
            # choose
            current_s += s[i]
            # explore
            if has_prefix(current_s, lst):
                find_anagrams_helper(s[:i]+s[i+1:], current_l, current_s, lst, long)
            # un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s, lst):
    """
    :param sub_s: If partial string do not exist in dictionary, early stopping function.
    :param lst: dictionary, stores all the exist words.
    """
    for ch in lst:
        if ch.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

#!/usr/bin/env python

#======================================================================#
# String-2                                                             #
# Medium python string problems -- 1 loop. Use + to combine strings,   #
# len(str) is the number of chars in a string, str[i:j] extracts the   #
# substring starting at index i and running up to but not including    #
# index j.                                                             #
#======================================================================#


# double_char
# Given a string, return a string where for every char in the original,
# there are two chars.
def double_char(str):
    result = ''
    for c in str:
        result += 2*c
    return result


# count_hi
# Return the number of times that the string "hi" appears anywhere in
# the given string.
def count_hi(str):
    return str.count('hi')


# cat_dog
# Return True if the string "cat" and "dog" appear the same number of
# times in the given string.
def cat_dog(str):
    return str.count('cat') == str.count('dog')


# count_code
# Return the number of times that the string "code" appears anywhere in
# the given string, except we'll accept any letter for the 'd', so
# "cope" and "cooe" count.
def count_code(str):
    count = 0
    for i in range(len(str)-3):
        sub = str[i:i+2] + str[i+3]
        if sub == 'coe':
            count += 1
    return count


# end_other
# Given two strings, return True if either of the strings appears at the very
# end of the other string, ignoring upper/lower case differences (in
# other words, the computation should not be "case sensitive"). Note:
# s.lower() returns the lowercase version of a string.
def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


# xyz_there
# Return True if the given string contains an appearance of "xyz" where
# the xyz is not directly preceeded by a period (.). So "xxyz" counts
# but "x.xyz" does not.
def xyz_there(str):
    for i in range(len(str)-2):
        sub = str[i:i+3]
        before_sub = str[i-1]
        if sub == 'xyz' and before_sub != '.':
            return True
    return False

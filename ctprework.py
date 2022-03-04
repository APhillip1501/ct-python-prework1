# Question 1:
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of code has been done below.


def hello_name(user_name):
    """Display a greeting."""
    print("Hello, " + user_name.title() + "!")

hello_name('bob')
hello_name('missy')


# Question 2:
# Write a python function, first_odds,
# that prints the odd numbers from 1-100
# and returns nothing.


def first_odd():
    odds = list(range(1,101,2))
    print(odds)
    return

first_odd()


# Question 3
# Please write a Python function, max_num_in_list,
# to return max number of a given list.
# First line of code has been done below.


def max_num_in_list(a_list):
    list = [1, 10, 100]
    for number in a_list:
        if number > 0
            print(max(a_list))

max_num_in_list(a_list)


# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not by 100,
# unless it is also divisible by 400.
# The return should be BOOLEAN type, (True/False.)


def is_leap_year(a_year):
    if (a_year % 4 = 0) 
    and (a_year % 100 != 0) 
    or (a_year % 400 = 0)
        return True
    else:
        return False 

a_year = 2022

is_leap_year(a_year)


# Question 5
# Write a function to check to see if all numbers 
# in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but, [1,2,4,5] are not consecutive numbers.
# The return should be BOOLEAN type.


def is_consecutive(a_list):
    numbers = (a_list(range[0:]))
    if number in numbers = a_list(0, 100, (+1)):
        return True
    else return False

is_consecutive(a_list) 


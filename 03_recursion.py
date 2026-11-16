

def print_n_numbers(n,current=1):
    if current > n:
        return
    
    print(current)
    return print_n_numbers(n, current+1)

def print_n_number_rev(n):
    if n < 1:
        return

    print(n)
    return print_n_number_rev(n-1) 

def print_n_times(n, string, current=0):
    if current >= n:
        return
    print(string)
    print_n_times(n, string, current+1)


def rec_fn(i,n):
    if i < 1:
        return 
    rec_fn(i-1, n)
    print(i)

# 1 -> n without using +
def print_n_numbers_back_tracking(n):
    rec_fn(n,n)

def rec_fn_2(i,n):
    if i > n:
        return 
    rec_fn_2(i+1, n)
    print(i)

# n -> 1 without using -
def print_n_numbers_back_tracking_2(n):
    rec_fn_2(1,n)

def sum_of_n_numbers(n, current=0, sum=0):
    if current > n:
        print(sum)
        return
    return sum_of_n_numbers(n, current=current+1, sum=sum + current)


def sum_of_n_numbers_functional(n):
    if n < 1:
        return 0
    return n +  sum_of_n_numbers_functional(n-1)


def factorial_n(n):
    if n <= 1:
        return 1

    return n * factorial_n(n-1)

# plain reverse
def reverse_arr(arr):
    if not arr:
        return arr
    end = len(arr) - 1
    start  = 0

    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start =start + 1
        end = end - 1 
    return arr


def swap_arr(arr, start, end):
    if start >= end:
        return arr
    arr[start],arr[end]= arr[end], arr[start]
    return swap_arr(arr, start+1, end-1)

def reverse_arr_recursion(arr, start=0, end=0):
    end = len(arr) - 1
    return swap_arr(arr, start, end)
    

def reverse_arr_single_var(arr, current=0):
    print(current,len(arr)-current-1 )
    if current >= len(arr)//2:
        return
    arr[current], arr[len(arr)-current-1] = arr[len(arr)-current-1], arr[current]
    reverse_arr_single_var(arr, current+1)
    return arr

import re
def palindrome_string(s, current=0):
    if s[current] != s[len(s)-1-current]:
        return False
    elif current >= len(s)//2:
        return True
    return palindrome_string(s, current+1)


def is_palindrome(s):
    s =s.lower()
    s = re.sub("[^a-zA-Z0-9]","",s)
    print(s)
    if not s:
        return True
    return palindrome_string(s) 



# multiple recursion calls
# fib series: 0 1 1 2 3 5 8 13 21 34
def get_nth_fib_number(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return get_nth_fib_number(n-1) + get_nth_fib_number(n-2)

n = int(input())
print(get_nth_fib_number(n))

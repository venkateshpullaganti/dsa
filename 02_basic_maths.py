import math



def count_digits(n):
    count = 0
    while n>=1:
        count = count + 1
        n = n/10

    # count = math.log10(n)+1 # log with base 10 is division by 10 of that n 
    print(count)    



def reverse_number(x):
    if x > math.pow(2,31) - 1 or x < math.pow(-2,31):
        return 0
    rev = 0
    is_neg = False
    if x < 0:
        is_neg = True
        x = x * -1
    while x > 0:
        ld = x % 10
        rev = (rev * 10)+ld
        x = x//10
    rev = rev * -1 if is_neg else rev
    return rev



def palindrome_num(x):
    rev = 0
    n = x
    is_neg = False
    if n < 0:
        is_neg = True
        n = n * -1
    
    while n >=1:
        ld = n % 10
        rev = (rev * 10)+ ld
        n = int(n/10)

    rev = rev * -1 if is_neg else rev
    if rev == x:
        print(True)
    else:
        print(False)



def armstrong_number(n):
# A number whose sum of cubes of its digits  the number
    cubes_sum = 0
    n_copy = n

    print(int(math.pow(2,3)))
    while n_copy > 0:
        digit = n_copy % 10
        cubes_sum = cubes_sum + digit ** 3
        n_copy = n_copy //10

        print(f"d -> {digit}")

    print(cubes_sum)
    if cubes_sum == n:
        print("Armstrong 💪 number")
        return True
    else:
        print("Not an armstrong 💪 number")
        return False
    


def divisors_of_n(n):
    divs = []
    for i in range(1, n+1):
        if n % i == 0:
            divs.append(i)

    return divs


def divisors_of_n_v2(n):
    divs = []
    i = 1
    while i * i < 36:
        if n % i == 0:
            divs.append(i)
            other_fac = n//i
            if other_fac == i:
                divs.append(other_fac)
        i = i+1
    divs.sort()
    return divs 


def is_prime(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count = count+1
            if n //i != i:
                count = count+1
        i = i + 1
    return count <= 2

# TC:  logn
def gcd_of_number(n1,n2):
    small = n2 if n1 > n2 else n1
    
    if max(n1,n2) % small == 0:
        return small
    
    gcd = 1
    i = 1

    while i * i <= small:
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
            on = n1 // i
            if n1 % on == 0 and n2 % on == 0 and on > i:
                gcd = on
        i = i+1 

    return gcd  



# Time complexity: logθ min(n1,n2)
def gcd_of_num_eucludian(n1,n2): 
        while n1 > 0 and n2 > 0:
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
        if n1 == 0: 
            return n2
        else:
            return n1




n = int(input())
n2 = int(input())
print(gcd_of_num_eucludian(n,n2))

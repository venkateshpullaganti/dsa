


def print_pattern4():
    '''
    *
    ***
    *****
    *******
    '''
    n = 5
    for i in range(1,n+1,1):
        spaces = (n-i) * " "
        starsL = i * "*"
        starsR = (i-1) * "*"
        print(spaces+starsL+starsR+spaces)

    # n = 5
    # for i in range(n):
    #     spaces = (n-i-1) * " "
    #     stars = (i*2+1) * "*"
    #     print(spaces+stars+spaces)


def print_pattern5():
    '''
    *
    ***
    *****
    *******
    '''
    # n = 5
    # for i in range(1,n+1,1):
    #     spaces = (n-i) * " "
    #     starsL = i * "*"
    #     starsR = (i-1) * "*"
    #     print(spaces+starsL+starsR+spaces)

    n = 5
    for i in range(n):
        for j in range(0,n-i-1,1):
            print(" ",end="")
        for j in range(0,i*2+1,1):
            print("*",end="")
        for j in range(0,n-i-1,1):
            print(" ",end="")

        print("")

# print_pattern5()

# def print_pattern6():
#     n=5
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for j in range(((n-i-1)*2)+1):
#             print("*",end="")
#         for j in range(i):
#             print(" ",end="")

# print_pattern6()

n = int(input())

def print_pattern22(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            top = j
            left = i
            right = (2*n-2)-j
            bottom = (2*n-2)-i
            d = min(top,bottom,left,right)
            print(n-d,end=" ")
        print("")


'''
3 3 3 3 3 
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
'''

print_pattern22(n)


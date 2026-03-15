

n = int(input())

def print_pattern(n):
    for i in range(n):
        for j in range(i):
            print("*",end=" ")
        print()


print_pattern(n)
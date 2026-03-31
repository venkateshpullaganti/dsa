def frequency_arr(size, arr, lookup_count, lookup_arr):
    hash_arr = [0 for i in range(13)]
    for i in arr:
        hash_arr[i] = hash_arr[i] + 1

    for i in lookup_arr:
            print(hash_arr[i])



size = int(input())
arr =[ int(i) for i in  input().split(" ")]
lookup_count = int(input())
lookup_arr =[int(i) for i in  input().split(" ")]
print(lookup_arr)

frequency_arr(size, arr, lookup_count, lookup_arr)
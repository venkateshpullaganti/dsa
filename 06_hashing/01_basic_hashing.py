
# int hasing
def frequency_arr(size, arr, lookup_count, lookup_arr):
    hash_arr = [0 for i in range(13)]
    for i in arr:
        hash_arr[i] = hash_arr[i] + 1

    for i in lookup_arr:
            print(hash_arr[i])


# char hasing 
def freq_arr_char(arr,lookup_arr):
    c_hash = [0 for i in range(27)]
    for i in arr:
        c_index = ord(i)-97
        c_hash[c_index] = c_hash[c_index] + 1
    for i in lookup_arr:
        c_index = ord(i) - 97
        print(c_hash[c_index])


# Return a list of pairs where each pair contains a unique element from the array and its frequency in the array.

def counting_freq(nums):
    freq_map = dict()
    for num in nums:
        if freq_map.get(num, 0)>0:
            freq_map[num] = freq_map.get(num) + 1
        else:
            freq_map[num] = 1

    arr = list()
    for k, i in freq_map.items():
        arr.append([k,i])

    print(arr)
    return arr
     



lookup_arr =[int(i) for i in  input().split(" ")]

counting_freq(lookup_arr)
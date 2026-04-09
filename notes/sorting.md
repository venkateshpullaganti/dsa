# 1. Selection Sort
**Core Intuition:** "Select the minimum and swap." You repeatedly find the smallest element from the unsorted part and place it at the beginning.

### Strategic Breakdown
* **The Mechanism:**
    1. Find the minimum element in the range `[i...n-1]`.
    2. Swap that minimum with the element at index `i`.
    3. Increment `i` and repeat until the array is sorted.
* **The "Aha!" Moment:** After every iteration `i`, the first `i+1` elements are sorted and will never be touched again.

### Complexity Analysis
* **Time Complexity:** $O(n^2)$ for Best, Average, and Worst cases. The inner loop always runs to find the minimum.
* **Space Complexity:** $O(1)$ (In-place sorting).

### Pro Tip
* **Stability:** Selection sort is **not stable** by default. It can change the relative order of equal elements because it performs long-distance swaps.
* **Loop Logic:** The outer loop only needs to run up to `n-2`. When the second-to-last element is placed, the last one is automatically sorted.

---

# 2. Bubble Sort
**Core Intuition:** "Push the maximum to the last." Repeatedly swap adjacent elements if they are in the wrong order.

### Strategic Breakdown
* **The Mechanism:**
    1. Compare adjacent elements `(j, j+1)`.
    2. If `arr[j] > arr[j+1]`, swap them.
    3. After one full pass, the largest element "bubbles up" to the last position.
    4. Repeat for the remaining unsorted portion.
* **Optimization:** Use a `didSwap` flag. If no swaps occur during a pass, the array is already sorted—**break early**.

### Complexity Analysis
* **Worst/Average Time:** $O(n^2)$ (Array is reverse sorted).
* **Best Time (Optimized):** $O(n)$ (Array is already sorted). **Crucial for interviews.**
* **Space Complexity:** $O(1)$.

### Pro Tip
* **Optimization is Key:** Always mention the `didSwap` flag optimization. It shows you care about the "Best Case" scenario and constant-time improvements.
* **Stability:** Bubble Sort is **stable** because it only swaps if an element is strictly greater, preserving the relative order of equal values.

---

# 3.Insertion Sort

Insertion sort is an intuitive sorting algorithm that builds a sorted array one element at a time. It is particularly efficient for small data sets or arrays that are already partially sorted.



## 1. How it Works (The Logic)
The algorithm conceptually maintains a **sorted** and an **unsorted** partition within the same array. It takes one element from the unsorted side and "drifts" it to its correct position in the sorted side.

* **Starting Point:** The first element (`index 0`) is always considered sorted by itself [00:31:57].
* **The Process:**
    1.  Pick the next element (let's call it the "target").
    2.  Compare the target with the element to its left.
    3.  If the left element is larger, **swap** them [00:33:13].
    4.  Continue swapping to the left until the target finds an element smaller than itself or reaches the start of the array [00:34:35].
    5.  Repeat until the end of the array is reached.

## 2. Dry Run Example
**Initial Array:** `[14, 9, 15, 12, 6]`

* **Iteration 1:** `14` is sorted.
* **Iteration 2 (Target 9):** Compare `9` and `14`. Swap. 
    * Result: `[9, 14, 15, 12, 6]` [00:32:19]
* **Iteration 3 (Target 15):** Compare `15` and `14`. $15 > 14$, so no swap.
    * Result: `[9, 14, 15, 12, 6]` [00:32:43]
* **Iteration 4 (Target 12):** * `12` vs `15` $\rightarrow$ Swap.
    * `12` vs `14` $\rightarrow$ Swap.
    * `12` vs `9` $\rightarrow$ Stop.
    * Result: `[9, 12, 14, 15, 6]` [00:32:49]
* **Iteration 5 (Target 6):** `6` swaps with `15`, `14`, `12`, and `9` until it reaches the front.
    * Final Result: `[6, 9, 12, 14, 15]` [00:34:35]

## 3. Code Implementation
This implementation uses a nested loop structure. The outer loop selects the element, and the inner `while` loop handles the shifting logic [00:36:48].

```cpp
void insertion_sort(int arr[], int n) {
    // Outer loop runs from 0 to n-1
    for (int i = 0; i <= n - 1; i++) {
        int j = i;
        
        // Inner loop: swap with the left neighbor 
        // as long as the left neighbor is greater
        while (j > 0 && arr[j - 1] > arr[j]) {
            int temp = arr[j - 1];
            arr[j - 1] = arr[j];
            arr[j] = temp;
            
            // Move index to the left to keep comparing
            j--; 
        }
    }
}
```

# 4. Merge Sort

Merge Sort is a highly efficient, stable, and comparison-based sorting algorithm. It follows the **Divide and Conquer** paradigm to sort an array [00:03:03].


## 1. Core Concept: Divide and Conquer
The algorithm works by repeatedly breaking down the array into smaller subarrays until each subarray consists of a single element (which is inherently sorted), and then merging those subarrays back together in a sorted manner.

* **Divide:** Find the middle index and split the array into two halves [00:04:03].
* **Conquer:** Recursively call merge sort on both halves until the base case is reached (array size $\leq 1$) [00:20:57].
* **Merge:** Combine the two sorted halves into one single sorted array [00:22:39].

## 2. Dry Run Example
**Array:** `[3, 2, 4, 1, 3]`

1.  **Divide:** Split into `[3, 2, 4]` and `[1, 3]`.
2.  **Divide Further:** `[3, 2, 4]` splits into `[3, 2]` and `[4]`. `[3, 2]` splits into `[3]` and `[2]`.
3.  **Merge (Smallest Units):** * Merge `[3]` and `[2]` $\rightarrow$ `[2, 3]`.
    * Merge `[2, 3]` and `[4]` $\rightarrow$ `[2, 3, 4]`.
4.  **Right Side:** `[1, 3]` splits into `[1]` and `[3]`, then merges back to `[1, 3]`.
5.  **Final Merge:** Merge `[2, 3, 4]` and `[1, 3]` $\rightarrow$ `[1, 2, 3, 3, 4]` [00:31:49].

## 3. Python Implementation
This implementation uses recursive calls for the division and a helper function for the merging logic [00:40:44].

```python
def merge_sort(arr, low, high):
    # Base Case: If the array has only one element
    if low >= high:
        return
    
    mid = (low + high) // 2
    
    # Recursively sort the left and right halves
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    
    # Merge the sorted halves
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    # Compare elements from both halves and add the smaller one to temp
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
            
    # Copy remaining elements from the left half, if any
    while left <= mid:
        temp.append(arr[left])
        left += 1
        
    # Copy remaining elements from the right half, if any
    while right <= high:
        temp.append(arr[right])
        right += 1
        
    # Transfer sorted elements from temp back to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

# Usage
nums = [3, 2, 4, 1, 3]
merge_sort(nums, 0, len(nums) - 1)
print(f"Sorted array: {nums}")
```


# 5. Quick Sort

Quick Sort is an advanced sorting algorithm that follows the **Divide and Conquer** paradigm. It is generally faster than Merge Sort in practice because it sorts the array in place without requiring an extra temporary array for merging [00:02:34].


## 1. How it Works (The Logic)
The core idea behind Quick Sort is to pick an element (called the **pivot**) and place it exactly where it belongs in the final sorted array. Once the pivot is in place, everything to its left is smaller, and everything to its right is larger [00:06:47].

* **Step 1: Pick a Pivot:** The pivot can be any element (first, last, middle, or random). We will use the **first element** as the pivot [00:04:13].
* **Step 2: Place the Pivot:** Find the correct index for the pivot such that all smaller elements are strictly on its left, and all larger elements are on its right [00:08:03].
* **Step 3: Recursion:** The pivot is now fixed. Recursively apply Step 1 and Step 2 to the left unsorted sub-array and the right unsorted sub-array [00:09:34].

## 2. The Partition Algorithm (Placing the Pivot)
How do we actually place the pivot in its correct position? We use two pointers: `i` and `j` [00:14:22].

1.  Set the pivot as the first element (`arr[low]`).
2.  Set pointer `i` at the `low` index (moving left to right).
3.  Set pointer `j` at the `high` index (moving right to left).
4.  **Move `i` forward** until you find an element *greater* than the pivot [00:14:46].
5.  **Move `j` backward** until you find an element *smaller* or equal to the pivot [00:15:18].
6.  If `i` is still less than `j`, **swap** `arr[i]` and `arr[j]` [00:15:37].
7.  Repeat steps 4-6 until `i` crosses `j` (`i > j`).
8.  Once `i` and `j` cross, the correct place for the pivot is found at index `j`. Swap the pivot (`arr[low]`) with `arr[j]` [00:17:53].

## 3. Python Implementation


```python
def quick_sort(arr, low, high):
    # Base Case: more than 1 element to sort
    if low < high:
        # Get the partition index where the pivot is placed
        p_index = partition(arr, low, high)
        
        # Recursively sort the left and right halves
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j:
        # Find first element greater than pivot from the left
        # (Bound condition: i <= high to avoid index out of bounds)
        while i <= high and arr[i] <= pivot:
            i += 1
            
        # Find first element smaller than pivot from the right
        # (Bound condition: j >= low to avoid index out of bounds)
        while j >= low and arr[j] > pivot:
            j -= 1
            
        # If pointers haven't crossed, swap elements to correct sides
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    # Pointers have crossed; swap pivot to its correct position (j)
    arr[low], arr[j] = arr[j], arr[low]
    
    # Return the correct position of the pivot
    return j

# Usage
nums = [4, 6, 2, 5, 7, 9, 1, 3]
quick_sort(nums, 0, len(nums) - 1)
print(f"Sorted array: {nums}")